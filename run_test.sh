#!/bin/sh

. ~/.venv/Scripts/activate

pip install requirements.txt

behave
