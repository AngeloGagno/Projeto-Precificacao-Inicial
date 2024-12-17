# **Precificação de Acomodações**

Este projeto tem como objetivo calcular a diária de apartamentos e armazenar essas informações em um banco de dados. Ele utiliza o **Streamlit** para a interface de usuário e o **Pydantic** para a validação dos dados. Aprecisa-se de informações como nome da acomodação, preço, tier (classificação), preço mínimo e preço base.

---

## **Funcionalidades** 🛠️

- **Entrada de dados**: O usuário fornece informações sobre a acomodação, como o nome, o valor da diária e o tier de classificação.
- **Validação de dados**: Os dados são validados usando o **Pydantic** antes de serem salvos.
- **Armazenamento**: Após validação, os dados são inseridos no banco de dados.
- **Interface amigável**: Utiliza o **Streamlit** para uma experiência de usuário fluida e visualmente agradável.

---

## **Tecnologias Utilizadas** 💻

- **Streamlit**: Para a criação da interface de usuário interativa.
- **Pydantic**: Para a validação e modelagem dos dados.
- **SQLAlchemy**: Para interagir com o banco de dados e persistir os dados.

---

## **Instalação e Execução** 🚀

Siga os passos abaixo para configurar o projeto localmente.

### 1. **Clone o repositório**

```bash
git clone https://github.com/AngeloGagno/Projeto-Precificacao-Inicial.git
cd Projeto-Precificacao-Inicial
```

### 2. **Crie um ambiente virtual(Opcional)**

```bash
python -m venv venv
source venv/bin/activate  # no macOS/Linux
venv\Scripts\activate     # no Windows
```

### 3. **Instale as Dependencias**
```bash
pip install -r requirements.txt
```
### 4. **Insira as Informacoes do Banco de Dados**
```
DATABASE_URL_ = "database:///example.db"
```

### 5. **Execute o aplicativo**
```bash
cd ./src/frontend
streamlit run app.py
```