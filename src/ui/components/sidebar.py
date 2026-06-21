import streamlit as st


MENU_PERMISSIONS = {
    "Dashboard": ("dashboard", "visualizar"),
    "Clientes": ("comercial", "visualizar"),
    "Contratos": ("comercial", "visualizar"),
    "Projetos": ("engenharia", "visualizar"),
    "Obras": ("obras", "visualizar"),
    "Financeiro": ("financeiro", "visualizar"),
    "Compras": ("compras", "visualizar"),
    "Estoque": ("estoque", "visualizar"),
    "RH": ("rh", "visualizar"),
    "Auditoria": ("auditoria", "visualizar"),
}


def render_sidebar() -> str:
    st.sidebar.title("UrbanPrime ERP")
    permissions = set(st.session_state.get("permissions", []))
    allowed = [name for name, perm in MENU_PERMISSIONS.items() if perm in permissions or ("admin", "all") in permissions or name == "Dashboard"]
    return st.sidebar.radio("Menu", allowed)
