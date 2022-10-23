from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.


zodiac_dict = {
    'aries': 'Aries is the first of the twelve zodiac signs and is represented by the constellation, the ram. If born '
             'under this sign, you\'re considered to be adventurous, dynamic, ambitious and competitive. Aries are '
             'known for their quickness and leadership qualities, as well as a tendency to be impulsive (blame the '
             '"fire" element) and blunt.',
    'taurus': 'Taurus is the second of the twelve zodiac signs and is represented by the constellation, Taurus. If '
              'born under this sign, you\'re considered to be dedicated, dependable, focused and creative. Tauruses '
              'are known for being intelligent and trustworthy, as well as stubborn (the sign is a bull, after all). '
              'Tauruses love to seek out pleasure and can be known to question authority.',
    'gemini': 'Gemini is the third of the twelve zodiac signs and is represented by the constellation Gemini, '
              'which is made up of the Dioscuri—the twins, Castor and Pollux. If born under this sign, '
              'you\'re considered to be energetic, expressive, intelligent and playful. Gemini are known for their '
              'outgoing nature and varied interests, but they have earned a (likely misplaced) reputation for being '
              'two-faced.',
    'cancer': 'Cancer is the fourth of the twelve zodiac signs and is represented by the constellation, Cancer, '
              'which is most often depicted as a crab. If born under this sign, you\'re considered to be bold, '
              'compassionate, protective and intuitive. Cancers are known for their care-giving nature, as well as a '
              'tendency to be distant and passive-aggressive.',
    'leo': 'Leo is the fifth of the twelve zodiac signs and is represented by the constellation, the lion. If born '
           'under this sign, you\'re considered to be vivacious, outgoing and fiery. Leos are known for their warm '
           'nature and high self-esteem, but they can have a tendency to be proud or jealous.',
    'virgo': 'Virgo is the sixth of the twelve zodiac signs and is represented by the constellation, the maiden. If '
             'born under this sign, you\'re considered to be practical, analytical and sophisticated. Virgos are '
             'known for their kindness and attention to detail, but they can have a tendency to be shy and have '
             'unfairly high standards for themselves and their loved ones.',
    'libra': 'Libra is the seventh of the twelve zodiac signs and is represented by the only inanimate constellation, '
             'the scales. If born under this sign, you\'re considered to be balanced, social and diplomatic. Libras '
             'are known for their selfless nature and companionship, but they can have a tendency to be too pragmatic '
             'and insecure.',
    'scorpio': 'Scorpio is the eighth of the twelve zodiac signs and is represented by the constellation, '
               'the scorpion. If born under this sign, you\'re considered to be loyal, resourceful and focused. '
               'Scorpios are known for their bravery and trailblazing nature, but they can appear prickly and closed '
               'off to strangers.',
    'sagittarius': 'Sagittarius is the ninth of the twelve zodiac signs and is represented by the constellation, '
                   'the archer. If born under this sign, you\'re considered to be optimistic, independent and '
                   'intellectual. Sagittariuses are known for being magnetic and generous, but they can have a '
                   'tendency to be arrogant and too direct.',
    'capricorn': 'Capricorn is the tenth of the twelve zodiac signs and is represented by the constellation, '
                 'the sea goat. If born under this sign, you\'re considered to be patient, hardworking and '
                 'disciplined. Capricorns are known for their tenacity and preference for boundaries and rules, '
                 'but they can have a tendency to be stubborn and too focused on perfection.',
    'aquarius': 'Aquarius is the eleventh of the twelve zodiac signs and is represented by the constellation, '
                'the water bearer. If born under this sign, you\'re considered to be innovative, loyal and original. '
                'Aquariuses are known for their creativity and rebellious nature, but they can have a tendency to be '
                'aloof with loved ones and uncompromising.',
    'pisces': 'Pisces is the final of the twelve zodiac signs and is represented by the constellation, the fishes. If '
              'born under this sign, you\'re considered to be intuitive, creative and empathetic. Pisces are known '
              'for their compassion and artistic nature, but they can have a tendency to be too sensitive or '
              'delusional.',
}


def zodiac(request, sign):
    description = zodiac_dict.get(sign)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponse(f'Zodiac sign "{sign}" not found')


def zodiac_int(request, sign):
    zodiac_list = list(zodiac_dict)
    if not sign or sign > len(zodiac_list):
        return HttpResponseNotFound(f'Zodiac number {sign} not found')
    else:
        return HttpResponseRedirect(f'/horoscope/{zodiac_list[sign - 1]}')
