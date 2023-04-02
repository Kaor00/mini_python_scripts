from tqdm import tqdm
from time import sleep
from progress.bar import Bar


for i in tqdm(range(10)):
    sleep(0.2)


bar = Bar('Processing', max=20)

for i in range(20):
    bar.next()
bar.finish()
# не отображается погресс
