from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        out = emotion_detector("I am glad this happened")
        self.assertEqual(out['dominant_emotion'], "joy")

        out = emotion_detector("I am really mad about this")
        self.assertEqual(out['dominant_emotion'], "anger")

        out = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(out['dominant_emotion'], "disgust")

        out = emotion_detector("I am so sad about this")
        self.assertEqual(out['dominant_emotion'], "sadness")

        out = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(out['dominant_emotion'], "fear")

unittest.main()
