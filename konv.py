import os

from unstructured.ingest.connector.sharepoint import (
    SharepointAccessConfig,
    SharepointPermissionsConfig,
    SimpleSharepointConfig,
)
from unstructured.ingest.interfaces import PartitionConfig, ProcessorConfig, ReadConfig
from unstructured.ingest.runner import SharePointRunner

if __name__ == "__main__":
    # Set your environment variables here if needed, or ensure they are set in your environment
    # For example, you can uncomment the line below and replace '<your_api_key>' with your actual API key
    # os.environ["UNSTRUCTURED_API_KEY"] = "<your_api_key>"

    runner = SharePointRunner(
        processor_config=ProcessorConfig(
            verbose=True,
            output_dir="sharepoint-ingest-output",
            num_processes=2,
        ),
        read_config=ReadConfig(),
        partition_config=PartitionConfig(
            partition_by_api=True,
            api_key="eZjegfFEQIcnWUqYmeNj5ZDRHGrCNy",  # Ensure this environment variable is set
        ),
        connector_config=SimpleSharepointConfig(
            access_config=SharepointAccessConfig(
                client_cred="p+yDreOuXYMvfymbUaftKjWwe6pON2MFh2wEfbmWN+k=",
            ),
            permissions_config=SharepointPermissionsConfig(
                application_id="538313f7-5541-476f-aff5-231d862bd01f",
                client_cred="jjM8Q~HuhCapSqq3q0adadiLnvxAT3HYqyLRycvU",
                tenant="38527d54-c928-4e12-b9aa-14a5023828f6",
            ),
            client_id="e3a58bd3-c0eb-40cc-8a66-b0e21a71756a",
            site="https://jankankovsky.sharepoint.com",
            # Adjust 'files_only' and 'path' parameters as needed
            files_only=True,
            path="Shared Documents",  # Update this path if necessary
        ),
    )
    runner.run()
