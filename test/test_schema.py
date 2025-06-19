import unittest
import requests

class TestMCPSchema(unittest.TestCase):
    def test_schema_endpoint(self):
        """Test that the MCP schema endpoint returns the expected structure"""
        # Make a request to the schema endpoint
        response = requests.get("http://localhost:7860/gradio_api/mcp/schema")
        
        # Check that the request was successful
        self.assertEqual(response.status_code, 200)
        
        # Parse the response as JSON
        schema = response.json()
        
        # Check that the schema is a list
        self.assertIsInstance(schema, list)
        
        # Check that the schema contains the sentiment_analysis tool
        self.assertTrue(any(tool["name"] == "sentiment_analysis" for tool in schema))
        
        # Find the sentiment_analysis tool
        sentiment_tool = next(tool for tool in schema if tool["name"] == "sentiment_analysis")
        
        # Check that the tool has the expected properties
        self.assertIn("description", sentiment_tool)
        self.assertIn("inputSchema", sentiment_tool)
        
        # Check that the inputSchema has the expected structure
        input_schema = sentiment_tool["inputSchema"]
        self.assertEqual(input_schema["type"], "object")
        self.assertIn("properties", input_schema)
        self.assertIn("text", input_schema["properties"])
        self.assertEqual(input_schema["properties"]["text"]["type"], "string")

if __name__ == "__main__":
    unittest.main()