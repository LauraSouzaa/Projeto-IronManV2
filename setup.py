# pip install cx_freeze
import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(
                   script="main.py", 
                   icon="assets/icone.ico",
                    target_name="NarutoSobrevivencia.exe"
                   ) ]
cx_Freeze.setup(
    name = "Naruto Sobrevivencia Ninja",
    description="Jogo de sobrevivência inspirado em Naruto",
    options={
        "build_exe":{
            "packages":["pygame","pyttsx3"],
            "include_files":["bases","recursos","log.dat"]
        }
    }, executables = executaveis
)

# python setup.py build
# python setup.py bdist_msi