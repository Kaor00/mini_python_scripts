import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

def generate_thread_veins_fast(width, height, n_branches=120, max_len_ratio=0.7, thickness_px=1.2):
    """
    Быстрая версия: нитевидные прожилки через локальные гауссианы.
    """
    veins = np.zeros((height, width), dtype=np.float32)

    # Размер окрестности для наложения (напр., ±3σ)
    radius = int(np.ceil(3 * thickness_px))
    y_grid, x_grid = np.ogrid[-radius:radius+1, -radius:radius+1]
    kernel = np.exp(-(x_grid**2 + y_grid**2) / (2 * thickness_px**2))
    kernel /= kernel.sum()  # нормализуем (не обязательно, но чисто)

    for _ in range(n_branches):
        # Случайная начальная точка на границе
        side = np.random.randint(4)
        if side == 0:      # слева
            x0, y0 = 0, np.random.rand() * height
        elif side == 1:    # сверху
            x0, y0 = np.random.rand() * width, 0
        elif side == 2:    # справа
            x0, y0 = width - 1, np.random.rand() * height
        else:              # снизу
            x0, y0 = np.random.rand() * width, height - 1

        path_len = int(np.random.uniform(0.3, max_len_ratio) * max(width, height))
        xs, ys = [x0], [y0]
        x, y = x0, y0

        for _ in range(path_len):
            dx = np.random.normal(0, 1.0)
            dy = np.random.normal(0, 1.0)
            if len(xs) > 1:
                prev_dx, prev_dy = xs[-1] - xs[-2], ys[-1] - ys[-2]
                dx = 0.6 * dx + 0.4 * prev_dx
                dy = 0.6 * dy + 0.4 * prev_dy
            x += dx
            y += dy
            x = np.clip(x, 0, width - 1)
            y = np.clip(y, 0, height - 1)
            xs.append(x)
            ys.append(y)

        # Интерполяция (опционально — можно убрать для скорости, оставить ломаную)
        t = np.linspace(0, 1, len(xs))
        fx = np.interp(np.linspace(0, 1, path_len * 2), t, xs)
        fy = np.interp(np.linspace(0, 1, path_len * 2), t, ys)

        # Накладываем гауссианы только в локальных окрестностях
        for xi, yi in zip(fx, fy):
            xi, yi = int(xi), int(yi)
            if 0 <= xi < width and 0 <= yi < height:
                # Локальная область
                y0_, x0_ = yi - radius, xi - radius
                y1_, x1_ = yi + radius + 1, xi + radius + 1
                if y0_ < 0: y0_, dy0 = 0, -y0_
                else: dy0 = 0
                if x0_ < 0: x0_, dx0 = 0, -x0_
                else: dx0 = 0
                if y1_ > height: y1_, dy1 = height, y1_ - height
                else: dy1 = 0
                if x1_ > width: x1_, dx1 = width, x1_ - width
                else: dx1 = 0

                # Вырезаем часть veins и kernel
                target = veins[y0_:y1_, x0_:x1_]
                k_part = kernel[dy0:kernel.shape[0]-dy1, dx0:kernel.shape[1]-dx1]
                # Обновляем максимум (чтобы нити не затирали друг друга)
                np.maximum(target, k_part * 0.9, out=target)

    return veins

# === Настройки ===
W, H = 1024, 1024
base_rgb = np.array([245, 243, 218]) / 255.0
emerald_rgb = np.array([0, 150, 136]) / 255.0

print("Генерация прожилок...")
veins = generate_thread_veins_fast(W, H, n_branches=100, max_len_ratio=0.7, thickness_px=1.0)
print("Прожилки готовы.")

# Формируем изображение
img = np.ones((H, W, 4), dtype=np.float32)
img[:, :, :3] = base_rgb
img[:, :, 3] = 0.5

alpha_veins = veins * 0.92
img[:, :, :3] = (1 - alpha_veins[..., None]) * img[:, :, :3] + alpha_veins[..., None] * emerald_rgb
img[:, :, 3] = np.maximum(img[:, :, 3], alpha_veins)

# Сохраняем
img_pil = Image.fromarray((img * 255).astype(np.uint8), 'RGBA')
img_pil.save("marble_emerald_fast.png")
print("✅ Сохранено: marble_emerald_fast.png")