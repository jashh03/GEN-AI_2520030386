This Week 2 experiment builds on basic API calls by organizing the LLM logic into a cleaner, modular structure. Instead of keeping everything in one script, 
"llm_client.py" encapsulates the model initialization and request handling, while "main.py" runs the core workflow using that client. 
It also introduces "test_client.py" to verify that the client behaves as expected, alongside "requirements.txt" to manage dependencies. Together,
these files show how to structure LLM integrations so they are easier to reuse, test, and scale.
