from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from .models import Question,Choice
from django.template import loader
from django.http import  Http404
from django.urls import reverse
from django.views import generic

# def index(request):
#     # return HttpResponse("Hello")
#
#     # last_ql = Question.objects.order_by('-pub_date')[:3]
#     # output = ','.join([q.question_text for q in last_ql])
#     # return HttpResponse(output)
#
#     # last_ql = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #  'last_ql': last_ql,
#     #     }
#     # return HttpResponse(template.render(context, request))
#
#     last_ql = Question.objects.order_by('-pub_date')[:5]
#     context = {'last_ql': last_ql}
#     #render()函数将请求对象作为第一个参数，模板名称作为第二个参数，字典作为其可选的第三个参数。它返回一个HttpResponse与给定上下文一起呈现的给定模板的。
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})
#     #get_list_or_404()函数，它的工作方式为get_object_or_404()-除使用filter()而不是get()。它引起了Http404如果列表是空的。
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:3]




class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def  detail (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render( request, 'polls/detail.html', {'question': question} )

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # print("request-->{},question-->{}".format(request.POST,question))
    try:
        # print("selected_choice-->",question.choice_set.get(pk=request.POST['choice']))
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print("selected_choice",selected_choice)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render( request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        } )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        return HttpResponseRedirect("/polls/{qid}/result".format(qid=question_id))
        # return HttpResponseRedirect("/polls/"+str(question_id)+"/results" )