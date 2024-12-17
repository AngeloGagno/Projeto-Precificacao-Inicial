from backend.schema import Acc_Price
from pydantic import ValidationError
from backend.models import Acc_PriceDB
from backend.database import get_db,Base,engine
import streamlit as st

def init_db():
    Base.metadata.create_all(engine)
    print("Tabelas criadas com sucesso.")


def validate_data(data: dict) -> Acc_Price:
    """Valida os dados usando Pydantic."""
    try:
        validated_data = Acc_Price(**data)
        print("Dados validados:", validated_data.model_dump())
        return validated_data
    except ValidationError as e:
        st.write("Erro de validação, verifique se o campo Nome Acomodacao está preenchida")
        raise


def insert_data(data,validated_data: Acc_Price,db:get_db):
    """Insere os dados validados no banco de dados."""
    session = db
    try:
        new_entry = Acc_PriceDB(**validated_data.model_dump())
        session.add(new_entry)
        session.commit()
        st.write("Dados inseridos com sucesso no banco.")
        st.write(f"Preco base: {round(data['base_price'],ndigits=0)} - Preco Minimo: {round(data['min_price'],ndigits=0)}")
    except Exception:
        st.write("Erro ao inserir dados verifique se o codigo do apartamento ja existe")
        session.rollback()
    finally:
        session.close()


def main(data):
    """Fluxo principal do programa."""
    init_db()
    try:
        validated_data = validate_data(data)
        insert_data(data,validated_data,get_db())   
    except Exception as e:
        print("Falha no processo:", e)


if __name__ == "__main__":
    main()