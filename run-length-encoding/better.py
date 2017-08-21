import re


class Method1(object):
    def decode(data):
        decoded = ''
        runs = re.findall('\d*\D', data)
        for run in runs:
            if len(run) > 1:
                decoded += int(run[:-1]) * run[-1]
            else:
                decoded += run
        return decoded


    def encode(data):
        encoded = ''
        runs = [m.group(0) for m in re.finditer('(\D)\\1*', data)]
        for run in runs:
            if len(run) > 1:
                encoded += str(len(run)) + run[0]
            else:
                encoded += run
        return encoded

class Method2(object):

    ENCODE_TEMPLATE = '[{}]+'

    def encode(string):
        """
        Encode a given string using run-length-encoding
        """
        idx = 0
        ret = list()
        while idx < len(string):
            c = string[idx]
            span = re.match(ENCODE_TEMPLATE.format(c), string[idx:]).span()[1]
            if span == 1:
                ret.append(str(c))
            else:
                ret.append(''.join([str(span), str(c)]))
            idx += span
        return ''.join(ret)

    DECODE_TEMPLATE = '[0-9]*[ a-zA-z]'

    def decode(string):
        """
        Decode run-length-encoded string back to normal
        """
        idx = 0
        ret = list()
        while idx < len(string):
            span = re.match(DECODE_TEMPLATE, string[idx:]).span()[1]
            if span == 1:
                ret.append(string[idx])
                idx += 1
            else:
                c = string[idx + span - 1]
                n = int(string[idx: idx + span - 1])
                for i in range(n):
                    ret.append(c)
                idx += span
        return ''.join(ret)
