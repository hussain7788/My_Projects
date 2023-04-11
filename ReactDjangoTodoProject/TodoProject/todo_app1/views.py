from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import datetime

# Create your views here.


class TodoApiVIew(APIView):
    def get(self, request, pk=None, format=None):
        print("id is::", pk)
        if pk is not None:
            try:
                obj = TodoModel.objects.get(id=pk)
            except:
                return Response({"Warning": "No Record Found"})
            ser = TodoSerializer(obj)
            return Response(ser.data)
        obj_all = TodoModel.objects.all()
        ser = TodoSerializer(obj_all, many=True)
        return Response(ser.data)

    def post(self, request, format=None):
       
        if request.query_params['section'] == "create":
            task_name = request.POST.get("task_name")
            print("task_name::", task_name)
            cr_time = timezone.now()
            due_date = timezone.now() + datetime.timedelta(days=5)
            todo_obj = TodoModel(t_name=task_name, t_cr_date=cr_time, t_due_date=due_date)
            todo_obj.save()
            s_todo_obj = TodoSerializer(todo_obj).data
            return Response(s_todo_obj, status=200)
        elif request.query_params['section'] == "mark_completed":
            todo_item_id = request.POST.get('todo_item_id', False)
            if todo_item_id is not False:
                try:
                    todo_obj = TodoModel.objects.get(id=int(todo_item_id))
                except:
                    return Response({"msg":"No Record Found"}, staus=400)
                else:
                    todo_obj.t_completed = 1
                    todo_obj.save()
                    s_todo_obj = TodoSerializer(todo_obj).data
                    return Response(s_todo_obj, status=200)
            else:
                return Response({"message": "Invalid Id"}, status=400)
        elif request.query_params['section'] == "filter":
            f_value = request.POST.get("filter_value", False)
            if f_value == "completed":
                f_todo_items_objs = TodoModel.objects.all().filter(t_completed=1)
                s_todo_obj = TodoSerializer(f_todo_items_objs, many=True).data
            elif f_value == "pending":
                f_todo_items_objs = TodoModel.objects.all().filter(t_completed=0)
                s_todo_obj = TodoSerializer(f_todo_items_objs, many=True).data
            elif f_value == "all_tasks":
                f_todo_items_objs = TodoModel.objects.all()
                s_todo_obj = TodoSerializer(f_todo_items_objs, many=True).data
            return Response(s_todo_obj, status=200)

        else:
            return Response({"message":"No Section Provided"})
                
    def delete(self, request, pk):
        todo_item_id = request.POST.get("todo_item_id", False)
        print("todo_item_id", todo_item_id)
        try:
            obj = TodoModel.objects.get(id=pk)
            print("deleted Obj::", obj)
        except:
            return Response({"message":"No record found"})
        else:
            obj.delete()
            todo_items_objs = TodoModel.objects.all()
            s_todo_obj = TodoSerializer(todo_items_objs, many=True).data
            return Response(s_todo_obj, status=200)
