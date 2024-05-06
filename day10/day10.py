# Importa módulos necessários
import os
from tkinter.filedialog import askdirectory

# Função para organizar arquivos
def organize_files():
    # Solicita ao usuário que selecione uma pasta raiz
    root_dir = askdirectory(title='Selecione uma pasta')
    
    # Obtém lista de arquivos na pasta raiz
    file_list = os.listdir(root_dir)

    # Dicionário que mapeia tipos de arquivos para suas respectivas extensões
    file_types = {
        'imagens': ['.png', '.jpg', '.CR2', '.webp', '.jpeg', '.raw'],
        'videos': ['.mp4', '.wmv'],
        '3d': ['.blend', '.blend1', '.stl', '.gcode', '.svg', '.3mf', '.mtl', '.dwg'],
        'planilhas': ['.xlsm', '.csv', '.xlsx', '.xls', '.XLS', '.sql', '.xltx'],
        'documentos': ['.docx', '.doc', '.pdf', '.pptx', '.txt'],
        'compactado': ['.zip', '.rar'],
        'instaladores': ['.exe', '.msi', '.iso'],
        'python': ['.py', '.pynb']
    }

    # Itera sobre cada arquivo na lista
    for file in file_list:
        # Obtém caminho e extensão do arquivo
        file_path, file_ext = os.path.splitext(os.path.join(root_dir, file))
        
        # Itera sobre cada tipo de arquivo e suas extensões
        for folder, extensions in file_types.items():
            # Verifica se a extensão do arquivo coincide com alguma das extensões do tipo de arquivo
            if file_ext.lower() in [ext.lower() for ext in extensions]:
                # Cria pasta para o tipo de arquivo se não existir
                folder_path = os.path.join(root_dir, folder)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                
                # Move o arquivo para a pasta correspondente
                os.rename(os.path.join(root_dir, file), os.path.join(folder_path, file))

# Executa a função organize_files se o script for executado diretamente
if __name__ == '__main__':
    organize_files()