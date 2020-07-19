"""
Automation for Internationalization of Languages
Can be plugged in robotframework
#Author:Sachin Dhiman
#Email: sachindhiman1@live.in
"""
from langdetect import detect
#from robot.api.deco import keyword, library


# @library
class LanguageValidator:
    """Class Implementation of Language Validator  """
    def __init__(self):
        self.valid_languages = [
            "af",
            "ar",
            "bg",
            "bn",
            "ca",
            "cs",
            "cy",
            "da",
            "de",
            "el",
            "en",
            "es",
            "et",
            "fa",
            "fi",
            "fr",
            "gu",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "kn",
            "ko",
            "lt",
            "lv",
            "mk",
            "ml",
            "mr",
            "ne",
            "nl",
            "no",
            "pa",
            "pl",
            "pt",
            "ro",
            "ru",
            "sk",
            "sl",
            "so",
            "sq",
            "sv",
            "sw",
            "ta",
            "te",
            "th",
            "tl",
            "tr",
            "uk",
            "ur",
            "vi",
            "zh-cn",
            "zh-tw",
        ]

    # @keyword
    def detect_input_language(self, expected_language, input_text):
        """
        Params: expected_language: input parameter to verify the input text,
                Valid Inputs:
                af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw
                input_text=Free Form text by user or automation tool
                        """
        if expected_language in self.valid_languages:

            return expected_language == str(detect(input_text))
        
        else:
            raise Exception("Language Out of Scope")
