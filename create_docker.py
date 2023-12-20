import platform
from dotenv import dotenv_values

def get_python_version():
    python_version = platform.python_version_tuple()
    return f'python:{python_version[0]}.{python_version[1]}-slim-buster'

def read_and_update_config(python_version):
    config = dotenv_values(".env")
    config["PYTHON_IMAGE"] = python_version

    # Set default port if not specified in .env file
    if 'FLASK_RUN_PORT' not in config:
        config['FLASK_RUN_PORT'] = '8000'

    return config

def generate_dockerfile(python_image, config):
    port = config['FLASK_RUN_PORT']
    with open("Dockerfile", "w") as file:
        file.write(f"FROM {python_image}\n")
        file.write("WORKDIR /usr/src/app\n")
        file.write("COPY . .\n")
        file.write("RUN pip install --no-cache-dir -r requirements.txt\n")
        file.write(f"EXPOSE {port}\n")
        for key, value in config.items():
            file.write(f"ENV {key}={value}\n")
        file.write(f'CMD ["flask", "run", "--port={port}"]\n')

if __name__ == "__main__":
    python_image = get_python_version()
    config = read_and_update_config(python_image)
    generate_dockerfile(python_image, config)
