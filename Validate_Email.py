from validate_email import validate_email as VE


is_valid = VE('watchdog@yan.ru')
print(is_valid)
# Фиктивная работа скрипта. Ощущение, что он проверяет лищь не пропущены ли буквы между @ и .
