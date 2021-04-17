import pickletools

def protocol_version(file_object):
    maxproto = -1
    for opcode, arg, pos in pickletools.genops(file_object):
        maxproto = max(maxproto, opcode.proto)
    return maxproto

#Getting the version of pickle protocol used.
with open('entry.pickle', 'rb') as f:
    v = pickleversion.protocol_version(f)
print (v)
#3

## Detailed information...
with open('entry.pickle', 'rb') as f:
     pickletools.dis(f)
#    0: \x80 PROTO      3
#    2: }    EMPTY_DICT
#    3: q    BINPUT     0
#    5: (    MARK
#    6: X        BINUNICODE 'published_date'
#   25: q        BINPUT     1
#   27: c        GLOBAL     'time struct_time'
#   45: q        BINPUT     2
#   47: (        MARK
#   48: M            BININT2    2009
#   51: K            BININT1    3
#   53: K            BININT1    27
#   55: K            BININT1    22
#   57: K            BININT1    20
#   59: K            BININT1    42
#   61: K            BININT1    4
#   63: K            BININT1    86
#   65: J            BININT     -1
#   70: t            TUPLE      (MARK at 47)
#   71: q        BINPUT     3
#   73: }        EMPTY_DICT
#   74: q        BINPUT     4
#   76: \x86     TUPLE2
#   77: q        BINPUT     5
#   79: R        REDUCE
#   80: q        BINPUT     6
#   82: X        BINUNICODE 'comments_link'
#  100: q        BINPUT     7
#  102: N        NONE
#  103: X        BINUNICODE 'internal_id'
#  119: q        BINPUT     8
#  121: C        SHORT_BINBYTES 'ÞÕ´ø'
#  127: q        BINPUT     9
#  129: X        BINUNICODE 'tags'
#  138: q        BINPUT     10
#  140: X        BINUNICODE 'diveintopython'
#  159: q        BINPUT     11
#  161: X        BINUNICODE 'docbook'
#  173: q        BINPUT     12
#  175: X        BINUNICODE 'html'
#  184: q        BINPUT     13
#  186: \x87     TUPLE3
#  187: q        BINPUT     14
#  189: X        BINUNICODE 'title'
#  199: q        BINPUT     15
#  201: X        BINUNICODE 'Dive into history, 2009 edition'
#  237: q        BINPUT     16
#  239: X        BINUNICODE 'article_link'
#  256: q        BINPUT     17
#  258: X        BINUNICODE 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
#  337: q        BINPUT     18
#  339: X        BINUNICODE 'published'
#  353: q        BINPUT     19
#  355: \x88     NEWTRUE
#  356: u        SETITEMS   (MARK at 5)
#  357: .    STOP
#highest protocol among opcodes = 3

