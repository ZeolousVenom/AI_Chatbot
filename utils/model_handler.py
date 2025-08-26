import ollama

class GemmaChatbot:
    def __init__(self, model_name="gemma3:1b"):
        self.model_name = model_name
        self.context = []
        
    def generate_response(self, user_input, temperature=0.7):
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[*self.context, {'role': 'user', 'content': user_input}],
                options={'temperature': temperature}
            )
            assistant_response = response['message']['content']
            self.context.extend([
                {'role': 'user', 'content': user_input},
                {'role': 'assistant', 'content': assistant_response}
            ])
            return assistant_response
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def clear_context(self):
        self.context = []