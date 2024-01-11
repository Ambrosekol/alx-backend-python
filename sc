mypy */*.py
pycodestyle */*.py
git add 0x00-python_variable_annotations
echo "enter commit msg: "
read msg
git commit -m "$msg"
git push