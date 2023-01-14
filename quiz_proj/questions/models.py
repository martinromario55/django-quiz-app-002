from django.db import models
from quizes.models import Quiz

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        # use reverse relation to get the answers. We can also use related_name="answers" on the question column of the answer table
        return self.answer_set.all() # answer.all()


# Answers Model
class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # We can add related_name="answer"
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question: {self.question.text}, Answer: {self.text}, Correct: {self.correct}"