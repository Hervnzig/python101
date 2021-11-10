import songs
import serializers

song = songs.Song('1', 'Water of love', 'Dire Straits')
serializer = serializers.ObjectSerializer()
result = serializer.serialize(song, 'JSON')
result_xml = serializer.serialize(song, 'XML')
# odd_result = serializer.serialize(song, 'XML2')

print(result)
print(result_xml)
# print(odd_result)

