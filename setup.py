import subprocess
import sys
import os

from setuptools import setup, find_packages

def run_script(script):
    subprocess.check_call(script, shell=True)

def all():
    run_script('./build.sh')

def clean():
    run_script('./build.sh clean')

def run():
    run_script('./build.sh web')

def dev():
    if 'CODESPACES' not in os.environ:
        run_script('./build.sh local_dev')
    else:
        run_script('./build.sh')
        run_script('./build.sh web')

def debug():
    run_script('./build.sh')
    run_script('./build.sh debug')

def deploy():
    run_script('./build.sh deploy')

def submit():
    run_script('juniorit submit')

commands = {
    'all': all,
    'clean': clean,
    'run': run,
    'dev': dev,
    'debug': debug,
    'deploy': deploy,
    'submit': submit,
}

def print_help_message():
    print("Available commands:\n")
    for command in commands:
        print(f"  {command}")
    print("")

# Check if a command is provided
if len(sys.argv) > 1:
    command = sys.argv[1]
    if command in commands:
        commands[command]()
    else:
        print(f'Unknown command {command}')
        print_help_message()
else:
    print_help_message()

setup(
    name='gamecraft',
    version='0.1',
    packages=find_packages(),
    # ... (other setup.py arguments)
)
