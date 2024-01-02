from selenium import webdriver

# Reemplaza 'tu_usuario' con tu nombre de usuario real en Windows.
# Asegúrate de que las barras invertidas en la ruta de Windows estén escapadas o usa barras normales.
driver = webdriver.Chrome(executable_path='C:/Users/tu_usuario/Downloads/chromedriver_win32/chromedriver')

driver.get('https://www.google.com')

# Tu código para interactuar con la página iría aquí

driver.quit()
