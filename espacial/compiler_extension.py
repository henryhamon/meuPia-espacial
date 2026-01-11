from meupia.analyzers.code_generator import CodeGenerator

class EspacialCodeGenerator(CodeGenerator):
    def __init__(self, symbol_table, output_file):
        super().__init__(symbol_table, output_file)
        
    def generate(self, root):
        """
        Gera o código Python, injetando os imports do plugin espacial.
        """
        # Injeta os imports necessários no topo do arquivo
        self.output_file.write("import sys\n")
        self.output_file.write("import krpc\n") # Embora o plugin use, o script final pode precisar também
        self.output_file.write("from espacial.plugin_ksp import *\n")
        self.output_file.write("\n")
        
        # Chama a geração padrão do Core
        super().generate(root)
        
    # Se houver necessidade de tratar funções específicas de forma diferente
    # na geração de código (ex: tradução de nomes), sobrescreva visit_FunctionCall aqui.
    # Por enquanto, como o Python permite chamar ksp_* direto se importado,
    # o comportamento padrão do CodeGenerator deve bastar.
