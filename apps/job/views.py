from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.views.generic import ListView

from apps.core.mixins import CreateListMixin
from .serializer import JobSerializer
from .models import Job
from .utils import create_object_from_field


class CreateJobAPI(CreateListMixin, generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        fields = ('company', ['company_size', 'company_type', 'industry'])
        serializer.initial_data = create_object_from_field(serializer.initial_data, fields)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AllJobsHandler(ListView):
    template_name = "all_jobs.html"
    context = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object_list = self._queryset()

    @staticmethod
    def _queryset():
        return Job.objects.all()

    def get(self, request, *args, **kwargs):
        self.context.update({
            'jobs': self.object_list
        })
        return self.render_to_response(self.context)


class JobsNextToYouHandler(ListView):
    template_name = "next_to_you.html"
    context = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object_list = self._queryset()

    @staticmethod
    def _queryset():
        return Job.objects.all()

    def get(self, request, *args, **kwargs):
        self.context.update({
            'nextToJobs': self.object_list
        })
        return self.render_to_response(self.context)


class RetrieveUpdateJobAPI(generics.RetrieveUpdateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'job_id'
