import logging
import os
import uuid
import base64

from typing import Dict

from ontology_dc8f06af066e4a7880a5938933236037.config import ConfigClass
from ontology_dc8f06af066e4a7880a5938933236037.input import InputClass
from ontology_dc8f06af066e4a7880a5938933236037.output import OutputClass
from openfabric_pysdk.context import AppModel, State

# Configurations for the app
configurations: Dict[str, ConfigClass] = dict()

############################################################
# Config callback function
############################################################
def config(configuration: Dict[str, ConfigClass], state: State) -> None:
    """
    Stores user-specific configuration data.

    Args:
        configuration (Dict[str, ConfigClass]): A mapping of user IDs to configuration objects.
        state (State): The current state of the application (not used in this implementation).
    """
    for uid, conf in configuration.items():
        logging.info(f"Saving new config for user with id:'{uid}'")
        configurations[uid] = conf


############################################################
# Execution callback function
############################################################
def execute(model: AppModel) -> None:
    """
    Main execution entry point for handling a model pass.

    Args:
        model (AppModel): The model object containing request and response structures.
    """

    # Retrieve input
    request: InputClass = model.request

    # Retrieve user config
    user_config: ConfigClass = configurations.get('super-user', None)
    logging.info(f"User config: {user_config}")

    # Get user prompt
    user_prompt = request.prompt
    logging.info(f"User Prompt: {user_prompt}")


    # Simulate text-to-image generation
    image_filename = f"output_{uuid.uuid4().hex}.png"
    image_path = os.path.join("/app/assets", image_filename)
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    # Write a fake 1x1 PNG image
    with open(image_path, "wb") as f:
        f.write(base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAEklEQVR42mP8z8BQDwADgwH/aCgTnQAAAABJRU5ErkJggg=="
        ))

    # Simulate image-to-3D output
    model_3d_filename = f"model_{uuid.uuid4().hex}.glb"
    model_3d_path = os.path.join("/app/assets", model_3d_filename)

    with open(model_3d_path, "w") as f:
        f.write("# Simulated 3D model content\n")

    # Prepare response
    response: OutputClass = model.response
    response.message = f"Generated 3D model for: {user_prompt}"
    response.image_path = image_path
    response.model_3d = model_3d_path