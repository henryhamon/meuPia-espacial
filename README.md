# meuPiá Espacial – Rocket Science Plugin

![meuPia](assets/meuPia-espacial.png)

## 📖 Overview

> **Nota:** Este é um **plugin oficial** para o compilador [meuPiá](https://www.google.com/search?q=https://github.com/SEU_USUARIO/meuPia-core).

**meuPiá Espacial** é a extensão de **Engenharia Aeroespacial** do ecossistema meuPiá.

Ele permite que estudantes controlem foguetes, aviões e rovers dentro do simulador **Kerbal Space Program (KSP)** utilizando algoritmos em Portugol. O plugin atua como uma ponte entre a lógica simples do aluno e o servidor de telemetria avançada do mod **kRPC**.

**meuPiá Espacial** fornece:

* **Mission Control API:** Comandos intuitivos (`ksp_travar_sas`, `ksp_acelerar`) para pilotar naves.
* **Telemetria em Tempo Real:** Funções para ler altitude, velocidade orbital, apoastro e combustível.
* **Automação de Voo:** Capacidade de criar pilotos automáticos completos, desde o lançamento até a aterrissagem.

## 🎯 Motivation

Aprender física e lógica de programação pode ser abstrato, mas ver seu código colocar um foguete em órbita torna o aprendizado tangível e emocionante.

**meuPiá Espacial** democratiza a "Rocket Science":

* **Baixa Barreira:** Scripts de kRPC em Python ou C# exigem conhecimento de Orientação a Objetos e APIs complexas. No meuPiá, o aluno usa comandos diretos: `ksp_ativar_estagio()`.
* **Física Aplicada:** O aluno aprende na prática conceitos de vetores, gravidade e mecânica orbital para resolver problemas (ex: "Acione o paraquedas se a velocidade vertical for negativa e altitude < 2000").

## ⚙️ How It Works

Este plugin utiliza o protocolo RPC (Remote Procedure Call) para conversar com o jogo:

### 1. The Connector

Ao usar o comando `ksp_conectar("Nome da Nave")`, o plugin estabelece uma conexão TCP com o servidor kRPC rodando dentro do jogo.

### 2. The Wrappers

O plugin traduz as chamadas complexas do kRPC (ex: `vessel.control.throttle = 1.0`) para funções nativas do Portugol (ex: `ksp_acelerar(1.0)`), gerenciando tipagem e tratamento de erros automaticamente.

### 3. The Code Generation

O Gerador de Código injeta as bibliotecas `krpc` e `protobuf` no script final Python, garantindo que a comunicação seja fluida e robusta.

---

## 🚀 Installation

Você pode instalar o pacote Espacial através do gerenciador de pacotes do meuPiá (`mpm`).

### Pré-requisitos

1. **Kerbal Space Program** (O Jogo) instalado.
2. **Mod kRPC** instalado no jogo (Disponível via CKAN ou GitHub do kRPC).

### Instalação do Plugin

```bash
# Instala o plugin no seu ambiente meuPiá
mpm install espacial

```

---

## 🛠️ Usage Examples

### 1. Lançamento Automático (Launch Script)

Um algoritmo simples para decolar, esperar sair da atmosfera densa e separar o estágio.

```portugol
algoritmo "LancarFoguete"
usar "espacial"

var altitude: real
inicio
    escreva("Iniciando contagem regressiva...")
    ksp_conectar("Vostok 1")
    
    ksp_travar_sas()
    ksp_acelerar(1.0) // Potência Máxima
    
    escreva("3... 2... 1... DECOLAR!")
    ksp_ativar_estagio()
    
    enquanto verdadeiro faca
        altitude <- ksp_obter_altitude()
        escreva("Altitude atual: ", altitude)
        
        // Separação de estágio aos 10km
        se altitude > 10000 entao
            escreva("Separando estágio principal...")
            ksp_ativar_estagio()
            pare // Encerra o loop
        fim_se
        
        esperar(1000)
    fimenquanto
fimalgoritmo

```

### 2. Controle de Pouso (Suicide Burn Logic)

Monitora a descida e aciona os motores no momento crítico.

```portugol
algoritmo "PousoAutomatico"
usar "espacial"

var 
    alt_solo: real
    vel_vert: real
inicio
    ksp_conectar("Lander")
    ksp_acelerar(0.0) // Motores desligados
    
    enquanto verdadeiro faca
        alt_solo <- ksp_obter_altitude_solo()
        vel_vert <- ksp_obter_velocidade_vertical()
        
        // Se estiver caindo rápido e perto do chão
        se (alt_solo < 500) e (vel_vert < -10) entao
            escreva("POUSO CRÍTICO! FREANDO!")
            ksp_acelerar(1.0)
        senao
            ksp_acelerar(0.0)
        fim_se
    fimenquanto
fimalgoritmo

```

---

## 📚 Supported Functions

Abaixo as principais funções disponíveis na versão v0.1:

| Função | Descrição |
| --- | --- |
| `ksp_conectar(nome)` | Conecta ao jogo e define o nome da nave na UI. |
| `ksp_acelerar(0.0 a 1.0)` | Controla a potência do motor (Throttle). |
| `ksp_ativar_estagio()` | Simula o aperto da barra de espaço (Staging). |
| `ksp_travar_sas()` | Ativa o sistema de estabilização (SAS). |
| `ksp_obter_apoastro()` | Retorna a altura máxima da órbita atual. |
| `ksp_obter_periastro()` | Retorna a altura mínima da órbita atual. |
| `ksp_obter_combustivel()` | Retorna a porcentagem de combustível restante. |

---

## 🙌 Credits

Desenvolvido como parte do ecossistema educacional **meuPiá** que é desenvolvido com ❤️ por **[@henryhamon](https://github.com/henryhamon)**.

* Core Compiler: [meuPia-core](https://github.com/henryhamon/meuPia-core.git)
* **Powered by:** [kRPC](https://krpc.github.io/krpc/) - The Remote Procedure Call Server for KSP.