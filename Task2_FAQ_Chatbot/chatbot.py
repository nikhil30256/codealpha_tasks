faq = {
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is python": "Python is a programming language.",
    "what is machine learning": "Machine Learning is a branch of AI."
}

print("FAQ Chatbot")
question = input("Ask a question: ").lower()

if question in faq:
    print(faq[question])
else:
    print("Sorry, answer not found.")
