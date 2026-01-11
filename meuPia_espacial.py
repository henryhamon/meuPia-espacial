import sys
import argparse
from meupia.analyzers.lexical_analyzer import LexicalAnalyzer
from meupia.analyzers.syntax_analyzer import SyntaxAnalyzer
from meupia.analyzers.semantic_analyzer import SemanticAnalyzer
from meupia.analyzers.symbol_table import SymbolTable
from espacial.compiler_extension import EspacialCodeGenerator

def main():
    parser = argparse.ArgumentParser(description="Compilador meuPia-Espacial para KSP")
    parser.add_argument("source_file", help="Arquivo fonte .por")
    args = parser.parse_args()

    source_path = args.source_file
    output_path = source_path.replace(".por", ".py")

    print(f"Compilando {source_path} para {output_path}...")

    try:
        # FASE 1: Análise Léxica
        lexer = LexicalAnalyzer(source_path)
        
        # FASE 2: Análise Sintática
        syntax = SyntaxAnalyzer(lexer)
        tree = syntax.parse()
        
        # FASE 3: Análise Semântica
        symbol_table = SymbolTable()
        semantic = SemanticAnalyzer(symbol_table)
        semantic.visit(tree)
        
        # FASE 4: Geração de Código (Com Extensão Espacial)
        with open(output_path, "w") as f:
            generator = EspacialCodeGenerator(symbol_table, f)
            generator.generate(tree)
            
        print("Compilação concluída com sucesso!")
        print(f"Execute com: python3 {output_path}")
        
    except Exception as e:
        print(f"Erro durante a compilação: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
