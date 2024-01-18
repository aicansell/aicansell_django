"""
# Initialize the recognizer
r = sr.Recognizer()

def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     

while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
 
            print("Did you say ",MyText)
            SpeakText(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")

"""
#whisper
"""
import openai
import wave
import pyaudio

openai.api_key =

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []


try:
   while True:
       data = stream.read(1024)
       frames.append(data)
except KeyboardInterrupt:
   pass


stream.stop_stream()
stream.close()
audio.terminate()


sound_file = wave.open("myrecording.wav", "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b"".join(frames))
sound_file.close()


audio_file = open("myrecording.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)


print(transcript['text'])

"""
  
def create(self, request):
        def process_user_data(userprofile_instance, user_power_words, user_weak_words, score, competencys, emotion_words):
            print("\n\nStarting Thread: UserProfile")
            userprofile_instance.scenarios_attempted += 1
            userprofile_instance.user_powerwords = (userprofile_instance.user_powerwords or '') + "," + ", ".join(user_power_words)
            userprofile_instance.user_weakwords = (userprofile_instance.user_weakwords or '') + "," + ", ".join(user_weak_words)
            userprofile_instance.user_powerwords = userprofile_instance.user_powerwords.strip(',')
            userprofile_instance.user_weakwords = userprofile_instance.user_weakwords.strip(',')
            if userprofile_instance.scenarios_attempted_score:
                userprofile_instance.scenarios_attempted_score += str(score) + ','
            else:
                userprofile_instance.scenarios_attempted_score = str(score) + ','
            print("\n\nCompleted Thread: UserProfile")
            print("\n\nStarting Thread: Update Competency")
            try:
                competency_score = json.loads(userprofile_instance.competency_score)
            except:
                competency_score = {}

            for competency in competencys:
                sub_competencies = competency.sub_competency.all()
                power_word_list = []
                negative_word_list = []

                for sub_competency in sub_competencies:
                    power_words = sub_competency.power_words.all()
                    negative_words = sub_competency.negative_words.all()

                    for power_word in power_words:
                        power_word_list.append(power_word.word.word_name.lower())

                    for negative_word in negative_words:
                        negative_word_list.append(negative_word.word.word_name.lower())

                power_word_count = 0
                negative_word_count = 0
                
                power_word_count = sum(1 for word in power_word_list if word in emotion_words)
                negative_word_count = sum(1 for word in negative_word_list if word in emotion_words)

                
                competency_name = str(competency.competency_name)
                        
                if competency_name in competency_score:
                    competency_score[competency_name] += ',' + str(power_word_count - negative_word_count)
                    competency_score[competency_name] = competency_score[competency_name]
                else:
                    competency_score[competency_name] = str(power_word_count - negative_word_count)

            userprofile_instance.competency_score = json.dumps(competency_score)
            userprofile_instance.save()
            print("\n\nCompleted Thread: Update Competency")
        
        """Create or update an item with emotion analysis."""
        instance = Item.objects.get(id=request.data.get('id'))
        userprofile_instance = UserProfile.objects.get(user=request.user)
        
        emotion_str = request.data.get('item_emotion').lower()

        competencys = instance.competencys.all().prefetch_related(
            'sub_competency__power_words__word',
            'sub_competency__negative_words__word'
        )

        power_word_list = []
        negative_word_list = []
        
        for competency in competencys:
            sub_competencies = competency.sub_competency.all()
            for sub_competency in sub_competencies:
                power_words = sub_competency.power_words.all()
                negative_words = sub_competency.negative_words.all()

                for power_word in power_words:
                    power_word_list.append(power_word.word.word_name.lower())

                for negative_word in negative_words:
                    negative_word_list.append(negative_word.word.word_name.lower())
                    
        user_text = emotion_str
                            
        instance.item_emotion = instance.item_emotion + ',' + emotion_str

        user_power_words = []
        user_weak_words = []
        
        for words in power_word_list:
            if words in emotion_str:
                user_power_words.append(words)
                instance.user_powerwords = (instance.user_powerwords or '') + "," + words + ','
        for words in negative_word_list:
            if words in emotion_str:
                user_weak_words.append(words)
                instance.user_weakwords = (instance.user_weakwords or '') + "," + words + ','

        score = len(user_power_words) - len(user_weak_words)

        instance.item_answercount += 1
        
        processing_thread = threading.Thread(
        target=process_user_data,
        args=(userprofile_instance, user_power_words, user_weak_words, score, competencys, user_text)
        )
        processing_thread.start()

        instance.save()
        
        data = {
            'id': instance.id,
            'item_name': instance.item_name,
            'coming_across_as': instance.coming_across_as
        }
        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)
       
        
        data = serialized_data.data

        response_data = {
            'id': data.get('id'),
            'item_name': data.get('item_name'),
            'coming_across_as': data.get('coming_across_as'),
            'compentency_score': score,
            'powerword_detected': user_power_words,
            'weekword_detected': user_weak_words,
            'power_word_list': power_word_list,
            'negative_word_list': negative_word_list,  
        }

        serialized_data = self.serializer_class(instance=instance, data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        response = {
            'status': 'Success',
            'data': response_data,
            'message': 'Item was successfully created.'
        }
        return Response(response, status=status.HTTP_201_CREATED)

