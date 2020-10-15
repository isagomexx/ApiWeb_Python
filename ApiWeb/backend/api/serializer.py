# from rest_framework.generics import ListAPIView
# from rest_framework import serializers

# # you're not serializing a model and since you want to display that count I guess, I'd suggest changing the serializer to this.
# class PacienteSerializer(serializers.Serializer):
#     # parameter1 = serializers.CharField(max_length=128, required=True)
#     # count = serializers.integerField(required=True)

#     class Meta:
#         fields = ('parameter1', 'count')

# class StatListView(ListAPIView):
#     queryset = Stat.objects.raw("SELECT parameter1, COUNT(*) FROM 
#                statistic_stat GROUP BY parameter1 order by count(*) desc 
#                LIMIT 10")
#     serializer_class = StatSerializer

#     def list(self, request):
#         queryset = self.get_queryset()
#         # the serializer didn't take my RawQuerySet, so made it into a list
#         serializer = StatSerializer(list(queryset), many=True)
#         return Response(serializer.data)