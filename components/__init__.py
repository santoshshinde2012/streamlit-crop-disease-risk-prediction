import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import streamlit.components.v1 as components
import json

load_dotenv()

if (os.getenv('DEV_MODE') == 'true' and os.getenv('FRONTEND_HOST')):
    _component_func = components.declare_component("chart", url="http://localhost:5173")
else:
    build_dir = Path(__file__).parent.absolute() / "chart/dist"
    _component_func = components.declare_component("chart", path=str(build_dir))


def rchart_events(fig):
    spec = json.dumps(fig)
    component_value = _component_func(spec=spec, default=None)
    return component_value
