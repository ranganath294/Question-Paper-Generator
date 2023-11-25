from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .functions import *


@api_view(['GET'])
def generate_question_paper(request):
    if request.method == 'GET':
        try:
            total_marks = request.data.get("total_marks", 100)
            subject = request.data.get("subject", None)
            easy_percentage = request.data.get("easy_percentage", 0)
            medium_percentage = request.data.get("medium_percentage", 0)
            hard_percentage = request.data.get("hard_percentage", 0)
            num_of_easy_ques = request.data.get("num_of_easy_ques", None)
            num_of_medium_ques = request.data.get("num_of_medium_ques", None)
            num_of_hard_ques = request.data.get("num_of_hard_ques", None)
            
            # Check if the necessary parameters are provided
            if not subject:
                return Response({"msg": "Fill all the fields"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if percentages sum to 100
            if easy_percentage + medium_percentage + hard_percentage == 100:
                # Calculate Marks From Percentages
                target_easy_marks = int(total_marks * (easy_percentage / 100))
                target_medium_marks = int(total_marks * (medium_percentage / 100))
                target_hard_marks = int(total_marks * (hard_percentage / 100))
                
                
                # Retrieve Questions in Sorted Order of Selected Subject
                easy_questions = Questions.objects.filter(subject=subject, difficulty='easy').order_by('marks')
                easy_que_marks = list(easy_questions.values_list('marks', flat=True))
                
                medium_questions = Questions.objects.filter(subject=subject, difficulty='medium').order_by('marks')
                medium_que_marks = list(medium_questions.values_list('marks', flat=True))
                
                hard_questions = Questions.objects.filter(subject=subject, difficulty='hard').order_by('marks')
                hard_que_marks = list(hard_questions.values_list('marks', flat=True))
                
                data = {}
                
                if num_of_easy_ques:
                    # Given Number of Easy Questions
                    easy_combinations = find_combinations_tabulation_num_ques(easy_que_marks, target_easy_marks, num_of_easy_ques)
                    data["easy_question_combinations"] = easy_combinations
                else:
                    easy_combinations = find_combinations_tabulation(easy_que_marks, target_easy_marks)
                    data["all_easy_question_combinations"] = easy_combinations
                
                if num_of_medium_ques:
                    # Given Number of Medium Questions
                    medium_combinations = find_combinations_tabulation_num_ques(medium_que_marks, target_medium_marks, num_of_medium_ques)
                    data["medium_question_combinations"] = medium_combinations
                else:
                    medium_combinations = find_combinations_tabulation(medium_que_marks, target_medium_marks)
                    data["all_medium_question_combinations"] = medium_combinations
                
                if num_of_hard_ques:
                    # Given Number of Hard Questions
                    hard_combinations = find_combinations_tabulation_num_ques(hard_que_marks, target_hard_marks, num_of_hard_ques)
                    data["hard_question_combinations"] = hard_combinations
                else:
                    hard_combinations = find_combinations_tabulation(hard_que_marks, target_hard_marks)
                    data["all_hard_question_combinations"] = hard_combinations
                
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"msg": "Total Percentage Marks should be 100"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # print(e)
            return Response({"msg": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)



# Creatinng New Question

@api_view(['POST'])
def create_question(request):
    if request.method == 'POST':
        try:
            question = request.data.get("question", None)
            subject = request.data.get("subject", None)
            topic = request.data.get("topic", None)
            difficulty = request.data.get("difficulty", None)
            marks = request.data.get("marks", None)
            
            question_instance = Questions.objects.create(question=question, subject=subject, topic=topic, difficulty=difficulty, marks=marks)
            question_instance.save()
            
            return Response({"msg": "Question Created Successfully"}, status=status.HTTP_200_OK)
            
        except Exception as e:
            # print(e)
            return Response({"msg": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)