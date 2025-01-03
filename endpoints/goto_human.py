from typing import Mapping, Dict, Any, Literal
from werkzeug import Request, Response
from dify_plugin import Endpoint
import json
import logging

class GotoHuman(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Implements the GoToHuman endpoint functionality
        """
        try:
            logging.info("====== Webhook Request Details ======")
            logging.info(f"Request Method: {r.method}")
            logging.info(f"Request Headers: {dict(r.headers)}")
            logging.info(f"Request Values: {values}")
            
            try:
                request_body = r.get_json()
                logging.info(f"Request Body: {json.dumps(request_body, indent=2)}")
            except Exception as e:
                logging.warning(f"Could not parse request body as JSON: {str(e)}")
                logging.info(f"Raw Request Body: {r.get_data(as_text=True)}")
            
            logging.info("================================")

            # Get request data and use it directly as workflow inputs
            data = r.get_json()
            workflow_inputs = {}
            for key, value in data.get("responseValues", {}).items():
                workflow_inputs[key] = value.get("value")
            
            app_id = settings.get('app_id', {}).get("app_id", "")
            logging.info(f"Processing webhook for app_id: {app_id}")
            logging.debug(f"Workflow inputs: {workflow_inputs}")
            
            # Call Dify workflow
            logging.info("Invoking Dify workflow")
            workflow_response = self.session.app.workflow.invoke(
                app_id=app_id,
                inputs=workflow_inputs,
                response_mode="blocking",
            )
            logging.info("Workflow execution completed successfully")
            logging.debug(f"Workflow response: {workflow_response}")

            return Response(
                json.dumps({
                    "status": "success",
                    "workflow_response": workflow_response
                }),
                status=200,
                content_type="application/json"
            )

        except Exception as e:
            logging.error(f"Error processing webhook: {str(e)}", exc_info=True)
            return Response(
                json.dumps({
                    "error": str(e)
                }),
                status=500,
                content_type="application/json"
            ) 