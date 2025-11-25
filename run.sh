#!/bin/bash
pip install -r requirements.txt
pytest -k mobile --disable-warnings -q
