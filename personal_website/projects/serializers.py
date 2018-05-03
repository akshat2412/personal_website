from rest_framework import serializers
from projects.models import Project, Technology

class TechnologySerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length = 40)

	class Meta:
		model = Technology
		fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
	
	# id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length = 50)
	summary = serializers.CharField()
	description = serializers.CharField()
	technology = TechnologySerializer(read_only = True, many = True)
	class Meta:
		model = Project
		fields = '__all__'
		


	def get_name(self, obj):
		 return obj.name