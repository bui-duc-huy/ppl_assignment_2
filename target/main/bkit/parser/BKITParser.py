# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u01bf\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\5\3\\\n\3\3\4\3\4\5\4`\n\4\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6l\n\6\3\7\3\7\5\7p\n\7\3\7\3\7\5\7")
        buf.write("t\n\7\3\b\3\b\3\b\3\b\5\bz\n\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\5\13\u0088\n\13\3\f\3\f")
        buf.write("\5\f\u008c\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u009d\n\17\3\20\3")
        buf.write("\20\3\20\5\20\u00a2\n\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u00ac\n\21\3\22\3\22\5\22\u00b0\n\22\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u00b6\n\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\5\24\u00c1\n\24\3\25\3\25\5")
        buf.write("\25\u00c5\n\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u00cf\n\26\3\26\3\26\5\26\u00d3\n\26\3\26\5\26\u00d6")
        buf.write("\n\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u00df\n")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u00e8\n\27")
        buf.write("\3\27\3\27\5\27\u00ec\n\27\3\30\3\30\5\30\u00f0\n\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u0109\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\5\37\u0122\n\37\3\37\3")
        buf.write("\37\7\37\u0126\n\37\f\37\16\37\u0129\13\37\3\37\3\37\3")
        buf.write("\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u015f\n")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u016a\n\"\f")
        buf.write("\"\16\"\u016d\13\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\7#\u017e\n#\f#\16#\u0181\13#\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\7$\u0195\n$\f")
        buf.write("$\16$\u0198\13$\3%\3%\3%\5%\u019d\n%\3&\3&\3&\3&\3&\3")
        buf.write("&\5&\u01a5\n&\3\'\3\'\3\'\3\'\3(\3(\3(\5(\u01ae\n(\3(")
        buf.write("\3(\3)\3)\3)\7)\u01b5\n)\f)\16)\u01b8\13)\3*\3*\3*\3*")
        buf.write("\3*\3*\2\5BDF+\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPR\2\3\3\2\26\27\2\u01d6")
        buf.write("\2T\3\2\2\2\4[\3\2\2\2\6_\3\2\2\2\ba\3\2\2\2\nk\3\2\2")
        buf.write("\2\fm\3\2\2\2\16y\3\2\2\2\20{\3\2\2\2\22\177\3\2\2\2\24")
        buf.write("\u0087\3\2\2\2\26\u0089\3\2\2\2\30\u008f\3\2\2\2\32\u0093")
        buf.write("\3\2\2\2\34\u009c\3\2\2\2\36\u009e\3\2\2\2 \u00ab\3\2")
        buf.write("\2\2\"\u00af\3\2\2\2$\u00b5\3\2\2\2&\u00c0\3\2\2\2(\u00c4")
        buf.write("\3\2\2\2*\u00ca\3\2\2\2,\u00eb\3\2\2\2.\u00ed\3\2\2\2")
        buf.write("\60\u00f3\3\2\2\2\62\u00fc\3\2\2\2\64\u010a\3\2\2\2\66")
        buf.write("\u0111\3\2\2\28\u0118\3\2\2\2:\u011b\3\2\2\2<\u011e\3")
        buf.write("\2\2\2>\u012d\3\2\2\2@\u015e\3\2\2\2B\u0160\3\2\2\2D\u016e")
        buf.write("\3\2\2\2F\u0182\3\2\2\2H\u019c\3\2\2\2J\u01a4\3\2\2\2")
        buf.write("L\u01a6\3\2\2\2N\u01aa\3\2\2\2P\u01b1\3\2\2\2R\u01b9\3")
        buf.write("\2\2\2TU\5\4\3\2UV\7\2\2\3V\3\3\2\2\2WX\5\6\4\2XY\5\4")
        buf.write("\3\2Y\\\3\2\2\2Z\\\5\6\4\2[W\3\2\2\2[Z\3\2\2\2\\\5\3\2")
        buf.write("\2\2]`\5\b\5\2^`\5\26\f\2_]\3\2\2\2_^\3\2\2\2`\7\3\2\2")
        buf.write("\2ab\7\24\2\2bc\7\65\2\2cd\5\n\6\2de\78\2\2e\t\3\2\2\2")
        buf.write("fg\5\f\7\2gh\7\67\2\2hi\5\n\6\2il\3\2\2\2jl\5\f\7\2kf")
        buf.write("\3\2\2\2kj\3\2\2\2l\13\3\2\2\2mo\7\3\2\2np\5\16\b\2on")
        buf.write("\3\2\2\2op\3\2\2\2ps\3\2\2\2qr\7\31\2\2rt\5\24\13\2sq")
        buf.write("\3\2\2\2st\3\2\2\2t\r\3\2\2\2uv\5\20\t\2vw\5\16\b\2wz")
        buf.write("\3\2\2\2xz\5\20\t\2yu\3\2\2\2yx\3\2\2\2z\17\3\2\2\2{|")
        buf.write("\7\63\2\2|}\7;\2\2}~\7\64\2\2~\21\3\2\2\2\177\u0080\7")
        buf.write("\3\2\2\u0080\u0081\5\16\b\2\u0081\23\3\2\2\2\u0082\u0088")
        buf.write("\7;\2\2\u0083\u0088\7<\2\2\u0084\u0088\t\2\2\2\u0085\u0088")
        buf.write("\7=\2\2\u0086\u0088\5\22\n\2\u0087\u0082\3\2\2\2\u0087")
        buf.write("\u0083\3\2\2\2\u0087\u0084\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0086\3\2\2\2\u0088\25\3\2\2\2\u0089\u008b\5\30")
        buf.write("\r\2\u008a\u008c\5\32\16\2\u008b\u008a\3\2\2\2\u008b\u008c")
        buf.write("\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\5\36\20\2\u008e")
        buf.write("\27\3\2\2\2\u008f\u0090\7\17\2\2\u0090\u0091\7\65\2\2")
        buf.write("\u0091\u0092\7\3\2\2\u0092\31\3\2\2\2\u0093\u0094\7\21")
        buf.write("\2\2\u0094\u0095\7\65\2\2\u0095\u0096\5\34\17\2\u0096")
        buf.write("\33\3\2\2\2\u0097\u0098\5\"\22\2\u0098\u0099\7\67\2\2")
        buf.write("\u0099\u009a\5\34\17\2\u009a\u009d\3\2\2\2\u009b\u009d")
        buf.write("\5\"\22\2\u009c\u0097\3\2\2\2\u009c\u009b\3\2\2\2\u009d")
        buf.write("\35\3\2\2\2\u009e\u009f\7\4\2\2\u009f\u00a1\7\65\2\2\u00a0")
        buf.write("\u00a2\5$\23\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\u00a3\3\2\2\2\u00a3\u00a4\5 \21\2\u00a4\u00a5\7")
        buf.write("\n\2\2\u00a5\u00a6\7\66\2\2\u00a6\37\3\2\2\2\u00a7\u00a8")
        buf.write("\5&\24\2\u00a8\u00a9\5 \21\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write("\u00ac\5&\24\2\u00ab\u00a7\3\2\2\2\u00ab\u00aa\3\2\2\2")
        buf.write("\u00ac!\3\2\2\2\u00ad\u00b0\7\3\2\2\u00ae\u00b0\5\22\n")
        buf.write("\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0#\3\2")
        buf.write("\2\2\u00b1\u00b2\5\b\5\2\u00b2\u00b3\5$\23\2\u00b3\u00b6")
        buf.write("\3\2\2\2\u00b4\u00b6\5\b\5\2\u00b5\u00b1\3\2\2\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b6%\3\2\2\2\u00b7\u00c1\5(\25\2\u00b8")
        buf.write("\u00c1\5*\26\2\u00b9\u00c1\5\60\31\2\u00ba\u00c1\5\64")
        buf.write("\33\2\u00bb\u00c1\5\66\34\2\u00bc\u00c1\58\35\2\u00bd")
        buf.write("\u00c1\5:\36\2\u00be\u00c1\5<\37\2\u00bf\u00c1\5> \2\u00c0")
        buf.write("\u00b7\3\2\2\2\u00c0\u00b8\3\2\2\2\u00c0\u00b9\3\2\2\2")
        buf.write("\u00c0\u00ba\3\2\2\2\u00c0\u00bb\3\2\2\2\u00c0\u00bc\3")
        buf.write("\2\2\2\u00c0\u00bd\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00bf")
        buf.write("\3\2\2\2\u00c1\'\3\2\2\2\u00c2\u00c5\7\3\2\2\u00c3\u00c5")
        buf.write("\5\22\n\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\u00c7\7\31\2\2\u00c7\u00c8\5@!\2")
        buf.write("\u00c8\u00c9\78\2\2\u00c9)\3\2\2\2\u00ca\u00cb\7\20\2")
        buf.write("\2\u00cb\u00cc\5@!\2\u00cc\u00ce\7\23\2\2\u00cd\u00cf")
        buf.write("\5$\23\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d2\5 \21\2\u00d1\u00d3\5,\27\2")
        buf.write("\u00d2\u00d1\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5\3")
        buf.write("\2\2\2\u00d4\u00d6\5.\30\2\u00d5\u00d4\3\2\2\2\u00d5\u00d6")
        buf.write("\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8\7\13\2\2\u00d8")
        buf.write("\u00d9\7\66\2\2\u00d9+\3\2\2\2\u00da\u00db\7\t\2\2\u00db")
        buf.write("\u00dc\5@!\2\u00dc\u00de\7\23\2\2\u00dd\u00df\5$\23\2")
        buf.write("\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\3")
        buf.write("\2\2\2\u00e0\u00e1\5 \21\2\u00e1\u00e2\5,\27\2\u00e2\u00ec")
        buf.write("\3\2\2\2\u00e3\u00e4\7\t\2\2\u00e4\u00e5\5@!\2\u00e5\u00e7")
        buf.write("\7\23\2\2\u00e6\u00e8\5$\23\2\u00e7\u00e6\3\2\2\2\u00e7")
        buf.write("\u00e8\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\5 \21\2")
        buf.write("\u00ea\u00ec\3\2\2\2\u00eb\u00da\3\2\2\2\u00eb\u00e3\3")
        buf.write("\2\2\2\u00ec-\3\2\2\2\u00ed\u00ef\7\b\2\2\u00ee\u00f0")
        buf.write("\5$\23\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00f1\3\2\2\2\u00f1\u00f2\5 \21\2\u00f2/\3\2\2\2\u00f3")
        buf.write("\u00f4\7\16\2\2\u00f4\u00f5\7\61\2\2\u00f5\u00f6\5\62")
        buf.write("\32\2\u00f6\u00f7\7\62\2\2\u00f7\u00f8\7\7\2\2\u00f8\u00f9")
        buf.write("\5 \21\2\u00f9\u00fa\7\f\2\2\u00fa\u00fb\7\66\2\2\u00fb")
        buf.write("\61\3\2\2\2\u00fc\u00fd\5\"\22\2\u00fd\u00fe\7\31\2\2")
        buf.write("\u00fe\u00ff\5@!\2\u00ff\u0100\3\2\2\2\u0100\u0101\7\67")
        buf.write("\2\2\u0101\u0102\5@!\2\u0102\u0108\7\67\2\2\u0103\u0104")
        buf.write("\5\"\22\2\u0104\u0105\7\31\2\2\u0105\u0106\5@!\2\u0106")
        buf.write("\u0109\3\2\2\2\u0107\u0109\5@!\2\u0108\u0103\3\2\2\2\u0108")
        buf.write("\u0107\3\2\2\2\u0109\63\3\2\2\2\u010a\u010b\7\25\2\2\u010b")
        buf.write("\u010c\5@!\2\u010c\u010d\7\7\2\2\u010d\u010e\5 \21\2\u010e")
        buf.write("\u010f\7\r\2\2\u010f\u0110\7\66\2\2\u0110\65\3\2\2\2\u0111")
        buf.write("\u0112\7\7\2\2\u0112\u0113\5 \21\2\u0113\u0114\7\25\2")
        buf.write("\2\u0114\u0115\5@!\2\u0115\u0116\7\r\2\2\u0116\u0117\7")
        buf.write("\66\2\2\u0117\67\3\2\2\2\u0118\u0119\7\5\2\2\u0119\u011a")
        buf.write("\78\2\2\u011a9\3\2\2\2\u011b\u011c\7\6\2\2\u011c\u011d")
        buf.write("\78\2\2\u011d;\3\2\2\2\u011e\u011f\7\3\2\2\u011f\u0121")
        buf.write("\7\61\2\2\u0120\u0122\5@!\2\u0121\u0120\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122\u0127\3\2\2\2\u0123\u0124\7\67\2")
        buf.write("\2\u0124\u0126\5@!\2\u0125\u0123\3\2\2\2\u0126\u0129\3")
        buf.write("\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012a")
        buf.write("\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b\7\62\2\2\u012b")
        buf.write("\u012c\78\2\2\u012c=\3\2\2\2\u012d\u012e\7\22\2\2\u012e")
        buf.write("\u012f\5@!\2\u012f\u0130\78\2\2\u0130?\3\2\2\2\u0131\u0132")
        buf.write("\5B\"\2\u0132\u0133\7&\2\2\u0133\u0134\5B\"\2\u0134\u015f")
        buf.write("\3\2\2\2\u0135\u0136\5B\"\2\u0136\u0137\7\'\2\2\u0137")
        buf.write("\u0138\5B\"\2\u0138\u015f\3\2\2\2\u0139\u013a\5B\"\2\u013a")
        buf.write("\u013b\7)\2\2\u013b\u013c\5B\"\2\u013c\u015f\3\2\2\2\u013d")
        buf.write("\u013e\5B\"\2\u013e\u013f\7-\2\2\u013f\u0140\5B\"\2\u0140")
        buf.write("\u015f\3\2\2\2\u0141\u0142\5B\"\2\u0142\u0143\7+\2\2\u0143")
        buf.write("\u0144\5B\"\2\u0144\u015f\3\2\2\2\u0145\u0146\5B\"\2\u0146")
        buf.write("\u0147\7/\2\2\u0147\u0148\5B\"\2\u0148\u015f\3\2\2\2\u0149")
        buf.write("\u014a\5B\"\2\u014a\u014b\7(\2\2\u014b\u014c\5B\"\2\u014c")
        buf.write("\u015f\3\2\2\2\u014d\u014e\5B\"\2\u014e\u014f\7*\2\2\u014f")
        buf.write("\u0150\5B\"\2\u0150\u015f\3\2\2\2\u0151\u0152\5B\"\2\u0152")
        buf.write("\u0153\7.\2\2\u0153\u0154\5B\"\2\u0154\u015f\3\2\2\2\u0155")
        buf.write("\u0156\5B\"\2\u0156\u0157\7,\2\2\u0157\u0158\5B\"\2\u0158")
        buf.write("\u015f\3\2\2\2\u0159\u015a\5B\"\2\u015a\u015b\7\60\2\2")
        buf.write("\u015b\u015c\5B\"\2\u015c\u015f\3\2\2\2\u015d\u015f\5")
        buf.write("B\"\2\u015e\u0131\3\2\2\2\u015e\u0135\3\2\2\2\u015e\u0139")
        buf.write("\3\2\2\2\u015e\u013d\3\2\2\2\u015e\u0141\3\2\2\2\u015e")
        buf.write("\u0145\3\2\2\2\u015e\u0149\3\2\2\2\u015e\u014d\3\2\2\2")
        buf.write("\u015e\u0151\3\2\2\2\u015e\u0155\3\2\2\2\u015e\u0159\3")
        buf.write("\2\2\2\u015e\u015d\3\2\2\2\u015fA\3\2\2\2\u0160\u0161")
        buf.write("\b\"\1\2\u0161\u0162\5D#\2\u0162\u016b\3\2\2\2\u0163\u0164")
        buf.write("\f\5\2\2\u0164\u0165\7%\2\2\u0165\u016a\5D#\2\u0166\u0167")
        buf.write("\f\4\2\2\u0167\u0168\7$\2\2\u0168\u016a\5D#\2\u0169\u0163")
        buf.write("\3\2\2\2\u0169\u0166\3\2\2\2\u016a\u016d\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016cC\3\2\2\2\u016d")
        buf.write("\u016b\3\2\2\2\u016e\u016f\b#\1\2\u016f\u0170\5F$\2\u0170")
        buf.write("\u017f\3\2\2\2\u0171\u0172\f\7\2\2\u0172\u0173\7\32\2")
        buf.write("\2\u0173\u017e\5F$\2\u0174\u0175\f\6\2\2\u0175\u0176\7")
        buf.write("\33\2\2\u0176\u017e\5F$\2\u0177\u0178\f\5\2\2\u0178\u0179")
        buf.write("\7\34\2\2\u0179\u017e\5F$\2\u017a\u017b\f\4\2\2\u017b")
        buf.write("\u017c\7\35\2\2\u017c\u017e\5F$\2\u017d\u0171\3\2\2\2")
        buf.write("\u017d\u0174\3\2\2\2\u017d\u0177\3\2\2\2\u017d\u017a\3")
        buf.write("\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180")
        buf.write("\3\2\2\2\u0180E\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0183")
        buf.write("\b$\1\2\u0183\u0184\5H%\2\u0184\u0196\3\2\2\2\u0185\u0186")
        buf.write("\f\b\2\2\u0186\u0187\7\36\2\2\u0187\u0195\5H%\2\u0188")
        buf.write("\u0189\f\7\2\2\u0189\u018a\7\37\2\2\u018a\u0195\5H%\2")
        buf.write("\u018b\u018c\f\6\2\2\u018c\u018d\7 \2\2\u018d\u0195\5")
        buf.write("H%\2\u018e\u018f\f\5\2\2\u018f\u0190\7!\2\2\u0190\u0195")
        buf.write("\5H%\2\u0191\u0192\f\4\2\2\u0192\u0193\7\"\2\2\u0193\u0195")
        buf.write("\5H%\2\u0194\u0185\3\2\2\2\u0194\u0188\3\2\2\2\u0194\u018b")
        buf.write("\3\2\2\2\u0194\u018e\3\2\2\2\u0194\u0191\3\2\2\2\u0195")
        buf.write("\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197G\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a\7#\2\2")
        buf.write("\u019a\u019d\5J&\2\u019b\u019d\5J&\2\u019c\u0199\3\2\2")
        buf.write("\2\u019c\u019b\3\2\2\2\u019dI\3\2\2\2\u019e\u01a5\5\24")
        buf.write("\13\2\u019f\u01a5\7\3\2\2\u01a0\u01a5\5L\'\2\u01a1\u01a5")
        buf.write("\5\22\n\2\u01a2\u01a5\5N(\2\u01a3\u01a5\5R*\2\u01a4\u019e")
        buf.write("\3\2\2\2\u01a4\u019f\3\2\2\2\u01a4\u01a0\3\2\2\2\u01a4")
        buf.write("\u01a1\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2")
        buf.write("\u01a5K\3\2\2\2\u01a6\u01a7\7\61\2\2\u01a7\u01a8\5@!\2")
        buf.write("\u01a8\u01a9\7\62\2\2\u01a9M\3\2\2\2\u01aa\u01ab\7\3\2")
        buf.write("\2\u01ab\u01ad\7\61\2\2\u01ac\u01ae\5P)\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\3\2\2\2\u01af")
        buf.write("\u01b0\7\62\2\2\u01b0O\3\2\2\2\u01b1\u01b6\5\24\13\2\u01b2")
        buf.write("\u01b3\7\67\2\2\u01b3\u01b5\5P)\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3")
        buf.write("\2\2\2\u01b7Q\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba")
        buf.write("\7\3\2\2\u01ba\u01bb\7\63\2\2\u01bb\u01bc\5@!\2\u01bc")
        buf.write("\u01bd\7\64\2\2\u01bdS\3\2\2\2&[_kosy\u0087\u008b\u009c")
        buf.write("\u00a1\u00ab\u00af\u00b5\u00c0\u00c4\u00ce\u00d2\u00d5")
        buf.write("\u00de\u00e7\u00eb\u00ef\u0108\u0121\u0127\u015e\u0169")
        buf.write("\u016b\u017d\u017f\u0194\u0196\u019c\u01a4\u01ad\u01b6")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Body'", "'Break'", "'Continue'", 
                     "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", 
                     "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
                     "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
                     "'True'", "'False'", "'EndDo'", "'='", "'+'", "'+.'", 
                     "'-'", "'-.'", "'*'", "'*.'", "'/'", "'/.'", "'%'", 
                     "'!'", "'||'", "'&&'", "'=='", "'!='", "'=/='", "'<'", 
                     "'<.'", "'>'", "'>.'", "'<='", "'<=.'", "'>='", "'>=.'", 
                     "'('", "')'", "'['", "']'", "':'", "'.'", "','", "';'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ID", "BODY", "BREAK", "CONTINUE", "DO", 
                      "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "ASSIGN", 
                      "ADDOP", "ADDOPDOT", "SUBOP", "SUBOPDOT", "MULOP", 
                      "MULOPDOT", "DIVOP", "DIVOPDOT", "MODOP", "NOTOP", 
                      "OROP", "ANDOP", "EQUALOP", "NOTEQUALOP", "NOTEQUALOPFLOAT", 
                      "LESSOP", "LESSOPDOT", "GREATEROP", "GREATEROPDOT", 
                      "LESSOREQUALOP", "LESSOREQUALOPDOT", "GREATEOREQUALOP", 
                      "GREATEOREQUALOPDOT", "LB", "RB", "LSB", "RSB", "COLON", 
                      "DOT", "COMMA", "SEMI", "LP", "RP", "INTLIT", "FLOATLIT", 
                      "STRINGLIT", "ARRAY", "WS", "COMMENT", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_many_declare = 1
    RULE_declare = 2
    RULE_var_declare = 3
    RULE_ids_list = 4
    RULE_id_declare = 5
    RULE_array_declares = 6
    RULE_array = 7
    RULE_array_id = 8
    RULE_type_list = 9
    RULE_func_declare = 10
    RULE_header_stm = 11
    RULE_paramater_stm = 12
    RULE_paramater_list = 13
    RULE_body_stm = 14
    RULE_statement_list = 15
    RULE_id_var = 16
    RULE_var_declare_list = 17
    RULE_statement = 18
    RULE_assign_statement = 19
    RULE_if_statement = 20
    RULE_else_if_statement = 21
    RULE_else_statement = 22
    RULE_for_statement = 23
    RULE_for_condition = 24
    RULE_while_statement = 25
    RULE_do_while_statement = 26
    RULE_break_statement = 27
    RULE_continue_statement = 28
    RULE_function_call_statement = 29
    RULE_return_statement = 30
    RULE_expressions = 31
    RULE_exp1 = 32
    RULE_exp2 = 33
    RULE_exp3 = 34
    RULE_exp4 = 35
    RULE_operand = 36
    RULE_sub_expression = 37
    RULE_function_call = 38
    RULE_list_expression = 39
    RULE_index_operator = 40

    ruleNames =  [ "program", "many_declare", "declare", "var_declare", 
                   "ids_list", "id_declare", "array_declares", "array", 
                   "array_id", "type_list", "func_declare", "header_stm", 
                   "paramater_stm", "paramater_list", "body_stm", "statement_list", 
                   "id_var", "var_declare_list", "statement", "assign_statement", 
                   "if_statement", "else_if_statement", "else_statement", 
                   "for_statement", "for_condition", "while_statement", 
                   "do_while_statement", "break_statement", "continue_statement", 
                   "function_call_statement", "return_statement", "expressions", 
                   "exp1", "exp2", "exp3", "exp4", "operand", "sub_expression", 
                   "function_call", "list_expression", "index_operator" ]

    EOF = Token.EOF
    ID=1
    BODY=2
    BREAK=3
    CONTINUE=4
    DO=5
    ELSE=6
    ELSEIF=7
    ENDBODY=8
    ENDIF=9
    ENDFOR=10
    ENDWHILE=11
    FOR=12
    FUNCTION=13
    IF=14
    PARAMETER=15
    RETURN=16
    THEN=17
    VAR=18
    WHILE=19
    TRUE=20
    FALSE=21
    ENDDO=22
    ASSIGN=23
    ADDOP=24
    ADDOPDOT=25
    SUBOP=26
    SUBOPDOT=27
    MULOP=28
    MULOPDOT=29
    DIVOP=30
    DIVOPDOT=31
    MODOP=32
    NOTOP=33
    OROP=34
    ANDOP=35
    EQUALOP=36
    NOTEQUALOP=37
    NOTEQUALOPFLOAT=38
    LESSOP=39
    LESSOPDOT=40
    GREATEROP=41
    GREATEROPDOT=42
    LESSOREQUALOP=43
    LESSOREQUALOPDOT=44
    GREATEOREQUALOP=45
    GREATEOREQUALOPDOT=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    COLON=51
    DOT=52
    COMMA=53
    SEMI=54
    LP=55
    RP=56
    INTLIT=57
    FLOATLIT=58
    STRINGLIT=59
    ARRAY=60
    WS=61
    COMMENT=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    UNTERMINATED_COMMENT=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def many_declare(self):
            return self.getTypedRuleContext(BKITParser.Many_declareContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.many_declare()
            self.state = 83
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare(self):
            return self.getTypedRuleContext(BKITParser.DeclareContext,0)


        def many_declare(self):
            return self.getTypedRuleContext(BKITParser.Many_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_declare" ):
                return visitor.visitMany_declare(self)
            else:
                return visitor.visitChildren(self)




    def many_declare(self):

        localctx = BKITParser.Many_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_many_declare)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.declare()
                self.state = 86
                self.many_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(BKITParser.Func_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)




    def declare(self):

        localctx = BKITParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.state = 91
                self.var_declare()
                pass
            elif token in [BKITParser.FUNCTION]:
                self.state = 92
                self.func_declare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ids_list(self):
            return self.getTypedRuleContext(BKITParser.Ids_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(BKITParser.VAR)
            self.state = 96
            self.match(BKITParser.COLON)
            self.state = 97
            self.ids_list()
            self.state = 98
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_declare(self):
            return self.getTypedRuleContext(BKITParser.Id_declareContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def ids_list(self):
            return self.getTypedRuleContext(BKITParser.Ids_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_ids_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds_list" ):
                return visitor.visitIds_list(self)
            else:
                return visitor.visitChildren(self)




    def ids_list(self):

        localctx = BKITParser.Ids_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ids_list)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.id_declare()

                self.state = 101
                self.match(BKITParser.COMMA)
                self.state = 102
                self.ids_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.id_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def array_declares(self):
            return self.getTypedRuleContext(BKITParser.Array_declaresContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def type_list(self):
            return self.getTypedRuleContext(BKITParser.Type_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_id_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_declare" ):
                return visitor.visitId_declare(self)
            else:
                return visitor.visitChildren(self)




    def id_declare(self):

        localctx = BKITParser.Id_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_id_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(BKITParser.ID)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.LSB:
                self.state = 108
                self.array_declares()


            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 111
                self.match(BKITParser.ASSIGN)
                self.state = 112
                self.type_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declaresContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def array_declares(self):
            return self.getTypedRuleContext(BKITParser.Array_declaresContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_declares

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declares" ):
                return visitor.visitArray_declares(self)
            else:
                return visitor.visitChildren(self)




    def array_declares(self):

        localctx = BKITParser.Array_declaresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_declares)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.array()

                self.state = 116
                self.array_declares()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(BKITParser.LSB)
            self.state = 122
            self.match(BKITParser.INTLIT)
            self.state = 123
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def array_declares(self):
            return self.getTypedRuleContext(BKITParser.Array_declaresContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_id" ):
                return visitor.visitArray_id(self)
            else:
                return visitor.visitChildren(self)




    def array_id(self):

        localctx = BKITParser.Array_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(BKITParser.ID)
            self.state = 126
            self.array_declares()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def array_id(self):
            return self.getTypedRuleContext(BKITParser.Array_idContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_type_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_list" ):
                return visitor.visitType_list(self)
            else:
                return visitor.visitChildren(self)




    def type_list(self):

        localctx = BKITParser.Type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_list)
        self._la = 0 # Token type
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(BKITParser.INTLIT)
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(BKITParser.FLOATLIT)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                _la = self._input.LA(1)
                if not(_la==BKITParser.TRUE or _la==BKITParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.match(BKITParser.STRINGLIT)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.array_id()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header_stm(self):
            return self.getTypedRuleContext(BKITParser.Header_stmContext,0)


        def body_stm(self):
            return self.getTypedRuleContext(BKITParser.Body_stmContext,0)


        def paramater_stm(self):
            return self.getTypedRuleContext(BKITParser.Paramater_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declare" ):
                return visitor.visitFunc_declare(self)
            else:
                return visitor.visitChildren(self)




    def func_declare(self):

        localctx = BKITParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.header_stm()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 136
                self.paramater_stm()


            self.state = 139
            self.body_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Header_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_header_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader_stm" ):
                return visitor.visitHeader_stm(self)
            else:
                return visitor.visitChildren(self)




    def header_stm(self):

        localctx = BKITParser.Header_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_header_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(BKITParser.FUNCTION)
            self.state = 142
            self.match(BKITParser.COLON)
            self.state = 143
            self.match(BKITParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramater_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def paramater_list(self):
            return self.getTypedRuleContext(BKITParser.Paramater_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_paramater_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamater_stm" ):
                return visitor.visitParamater_stm(self)
            else:
                return visitor.visitChildren(self)




    def paramater_stm(self):

        localctx = BKITParser.Paramater_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paramater_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(BKITParser.PARAMETER)
            self.state = 146
            self.match(BKITParser.COLON)
            self.state = 147
            self.paramater_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramater_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_var(self):
            return self.getTypedRuleContext(BKITParser.Id_varContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def paramater_list(self):
            return self.getTypedRuleContext(BKITParser.Paramater_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_paramater_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamater_list" ):
                return visitor.visitParamater_list(self)
            else:
                return visitor.visitChildren(self)




    def paramater_list(self):

        localctx = BKITParser.Paramater_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramater_list)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.id_var()

                self.state = 150
                self.match(BKITParser.COMMA)
                self.state = 151
                self.paramater_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.id_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_body_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_stm" ):
                return visitor.visitBody_stm(self)
            else:
                return visitor.visitChildren(self)




    def body_stm(self):

        localctx = BKITParser.Body_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_body_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(BKITParser.BODY)
            self.state = 157
            self.match(BKITParser.COLON)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 158
                self.var_declare_list()


            self.state = 161
            self.statement_list()
            self.state = 162
            self.match(BKITParser.ENDBODY)
            self.state = 163
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(BKITParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = BKITParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement_list)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.statement()
                self.state = 166
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def array_id(self):
            return self.getTypedRuleContext(BKITParser.Array_idContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_id_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_var" ):
                return visitor.visitId_var(self)
            else:
                return visitor.visitChildren(self)




    def id_var(self):

        localctx = BKITParser.Id_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_id_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 171
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 172
                self.array_id()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declare_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_declare_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare_list" ):
                return visitor.visitVar_declare_list(self)
            else:
                return visitor.visitChildren(self)




    def var_declare_list(self):

        localctx = BKITParser.Var_declare_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_declare_list)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.var_declare()
                self.state = 176
                self.var_declare_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.var_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_statement(self):
            return self.getTypedRuleContext(BKITParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(BKITParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BKITParser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(BKITParser.While_statementContext,0)


        def do_while_statement(self):
            return self.getTypedRuleContext(BKITParser.Do_while_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKITParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(BKITParser.Continue_statementContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(BKITParser.Function_call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKITParser.Return_statementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.while_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 185
                self.do_while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 186
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 187
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 188
                self.function_call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 189
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def array_id(self):
            return self.getTypedRuleContext(BKITParser.Array_idContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = BKITParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 192
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 193
                self.array_id()
                pass


            self.state = 196
            self.match(BKITParser.ASSIGN)
            self.state = 197
            self.expressions()
            self.state = 198
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def else_if_statement(self):
            return self.getTypedRuleContext(BKITParser.Else_if_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(BKITParser.Else_statementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = BKITParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(BKITParser.IF)
            self.state = 201
            self.expressions()
            self.state = 202
            self.match(BKITParser.THEN)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 203
                self.var_declare_list()


            self.state = 206
            self.statement_list()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSEIF:
                self.state = 207
                self.else_if_statement()


            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 210
                self.else_statement()


            self.state = 213
            self.match(BKITParser.ENDIF)
            self.state = 214
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def else_if_statement(self):
            return self.getTypedRuleContext(BKITParser.Else_if_statementContext,0)


        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_statement" ):
                return visitor.visitElse_if_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_if_statement(self):

        localctx = BKITParser.Else_if_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_else_if_statement)
        self._la = 0 # Token type
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(BKITParser.ELSEIF)
                self.state = 217
                self.expressions()
                self.state = 218
                self.match(BKITParser.THEN)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.VAR:
                    self.state = 219
                    self.var_declare_list()


                self.state = 222
                self.statement_list()

                self.state = 223
                self.else_if_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(BKITParser.ELSEIF)
                self.state = 226
                self.expressions()
                self.state = 227
                self.match(BKITParser.THEN)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.VAR:
                    self.state = 228
                    self.var_declare_list()


                self.state = 231
                self.statement_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = BKITParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(BKITParser.ELSE)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 236
                self.var_declare_list()


            self.state = 239
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def for_condition(self):
            return self.getTypedRuleContext(BKITParser.For_conditionContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = BKITParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(BKITParser.FOR)
            self.state = 242
            self.match(BKITParser.LB)
            self.state = 243
            self.for_condition()
            self.state = 244
            self.match(BKITParser.RB)
            self.state = 245
            self.match(BKITParser.DO)
            self.state = 246
            self.statement_list()
            self.state = 247
            self.match(BKITParser.ENDFOR)
            self.state = 248
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def expressions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionsContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionsContext,i)


        def id_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Id_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Id_varContext,i)


        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ASSIGN)
            else:
                return self.getToken(BKITParser.ASSIGN, i)

        def getRuleIndex(self):
            return BKITParser.RULE_for_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_condition" ):
                return visitor.visitFor_condition(self)
            else:
                return visitor.visitChildren(self)




    def for_condition(self):

        localctx = BKITParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.id_var()
            self.state = 251
            self.match(BKITParser.ASSIGN)
            self.state = 252
            self.expressions()
            self.state = 254
            self.match(BKITParser.COMMA)
            self.state = 255
            self.expressions()
            self.state = 256
            self.match(BKITParser.COMMA)
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 257
                self.id_var()
                self.state = 258
                self.match(BKITParser.ASSIGN)
                self.state = 259
                self.expressions()
                pass

            elif la_ == 2:
                self.state = 261
                self.expressions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = BKITParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(BKITParser.WHILE)
            self.state = 265
            self.expressions()
            self.state = 266
            self.match(BKITParser.DO)
            self.state = 267
            self.statement_list()
            self.state = 268
            self.match(BKITParser.ENDWHILE)
            self.state = 269
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_statement" ):
                return visitor.visitDo_while_statement(self)
            else:
                return visitor.visitChildren(self)




    def do_while_statement(self):

        localctx = BKITParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(BKITParser.DO)
            self.state = 272
            self.statement_list()
            self.state = 273
            self.match(BKITParser.WHILE)
            self.state = 274
            self.expressions()
            self.state = 275
            self.match(BKITParser.ENDWHILE)
            self.state = 276
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = BKITParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(BKITParser.BREAK)
            self.state = 279
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = BKITParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(BKITParser.CONTINUE)
            self.state = 282
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expressions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionsContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_function_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_statement" ):
                return visitor.visitFunction_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_call_statement(self):

        localctx = BKITParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_function_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(BKITParser.ID)
            self.state = 285
            self.match(BKITParser.LB)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.NOTOP) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 286
                self.expressions()


            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 289
                self.match(BKITParser.COMMA)
                self.state = 290
                self.expressions()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 296
            self.match(BKITParser.RB)
            self.state = 297
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = BKITParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(BKITParser.RETURN)
            self.state = 300
            self.expressions()
            self.state = 301
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def EQUALOP(self):
            return self.getToken(BKITParser.EQUALOP, 0)

        def NOTEQUALOP(self):
            return self.getToken(BKITParser.NOTEQUALOP, 0)

        def LESSOP(self):
            return self.getToken(BKITParser.LESSOP, 0)

        def LESSOREQUALOP(self):
            return self.getToken(BKITParser.LESSOREQUALOP, 0)

        def GREATEROP(self):
            return self.getToken(BKITParser.GREATEROP, 0)

        def GREATEOREQUALOP(self):
            return self.getToken(BKITParser.GREATEOREQUALOP, 0)

        def NOTEQUALOPFLOAT(self):
            return self.getToken(BKITParser.NOTEQUALOPFLOAT, 0)

        def LESSOPDOT(self):
            return self.getToken(BKITParser.LESSOPDOT, 0)

        def LESSOREQUALOPDOT(self):
            return self.getToken(BKITParser.LESSOREQUALOPDOT, 0)

        def GREATEROPDOT(self):
            return self.getToken(BKITParser.GREATEROPDOT, 0)

        def GREATEOREQUALOPDOT(self):
            return self.getToken(BKITParser.GREATEOREQUALOPDOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expressions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions" ):
                return visitor.visitExpressions(self)
            else:
                return visitor.visitChildren(self)




    def expressions(self):

        localctx = BKITParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expressions)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.exp1(0)
                self.state = 304
                self.match(BKITParser.EQUALOP)
                self.state = 305
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.exp1(0)
                self.state = 308
                self.match(BKITParser.NOTEQUALOP)
                self.state = 309
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.exp1(0)
                self.state = 312
                self.match(BKITParser.LESSOP)
                self.state = 313
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 315
                self.exp1(0)
                self.state = 316
                self.match(BKITParser.LESSOREQUALOP)
                self.state = 317
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 319
                self.exp1(0)
                self.state = 320
                self.match(BKITParser.GREATEROP)
                self.state = 321
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 323
                self.exp1(0)
                self.state = 324
                self.match(BKITParser.GREATEOREQUALOP)
                self.state = 325
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 327
                self.exp1(0)
                self.state = 328
                self.match(BKITParser.NOTEQUALOPFLOAT)
                self.state = 329
                self.exp1(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 331
                self.exp1(0)
                self.state = 332
                self.match(BKITParser.LESSOPDOT)
                self.state = 333
                self.exp1(0)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 335
                self.exp1(0)
                self.state = 336
                self.match(BKITParser.LESSOREQUALOPDOT)
                self.state = 337
                self.exp1(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 339
                self.exp1(0)
                self.state = 340
                self.match(BKITParser.GREATEROPDOT)
                self.state = 341
                self.exp1(0)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 343
                self.exp1(0)
                self.state = 344
                self.match(BKITParser.GREATEOREQUALOPDOT)
                self.state = 345
                self.exp1(0)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 347
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def ANDOP(self):
            return self.getToken(BKITParser.ANDOP, 0)

        def OROP(self):
            return self.getToken(BKITParser.OROP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 361
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 359
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 353
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 354
                        self.match(BKITParser.ANDOP)
                        self.state = 355
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 356
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 357
                        self.match(BKITParser.OROP)
                        self.state = 358
                        self.exp2(0)
                        pass

             
                self.state = 363
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def ADDOP(self):
            return self.getToken(BKITParser.ADDOP, 0)

        def ADDOPDOT(self):
            return self.getToken(BKITParser.ADDOPDOT, 0)

        def SUBOP(self):
            return self.getToken(BKITParser.SUBOP, 0)

        def SUBOPDOT(self):
            return self.getToken(BKITParser.SUBOPDOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 379
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 367
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 368
                        self.match(BKITParser.ADDOP)
                        self.state = 369
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 370
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 371
                        self.match(BKITParser.ADDOPDOT)
                        self.state = 372
                        self.exp3(0)
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 373
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 374
                        self.match(BKITParser.SUBOP)
                        self.state = 375
                        self.exp3(0)
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 376
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 377
                        self.match(BKITParser.SUBOPDOT)
                        self.state = 378
                        self.exp3(0)
                        pass

             
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MULOP(self):
            return self.getToken(BKITParser.MULOP, 0)

        def MULOPDOT(self):
            return self.getToken(BKITParser.MULOPDOT, 0)

        def DIVOP(self):
            return self.getToken(BKITParser.DIVOP, 0)

        def DIVOPDOT(self):
            return self.getToken(BKITParser.DIVOPDOT, 0)

        def MODOP(self):
            return self.getToken(BKITParser.MODOP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 404
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 402
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 387
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 388
                        self.match(BKITParser.MULOP)
                        self.state = 389
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 390
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 391
                        self.match(BKITParser.MULOPDOT)
                        self.state = 392
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 393
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 394
                        self.match(BKITParser.DIVOP)
                        self.state = 395
                        self.exp4()
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 396
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 397
                        self.match(BKITParser.DIVOPDOT)
                        self.state = 398
                        self.exp4()
                        pass

                    elif la_ == 5:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 399
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 400
                        self.match(BKITParser.MODOP)
                        self.state = 401
                        self.exp4()
                        pass

             
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTOP(self):
            return self.getToken(BKITParser.NOTOP, 0)

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp4)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(BKITParser.NOTOP)
                self.state = 408
                self.operand()
                pass
            elif token in [BKITParser.ID, BKITParser.TRUE, BKITParser.FALSE, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_list(self):
            return self.getTypedRuleContext(BKITParser.Type_listContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def sub_expression(self):
            return self.getTypedRuleContext(BKITParser.Sub_expressionContext,0)


        def array_id(self):
            return self.getTypedRuleContext(BKITParser.Array_idContext,0)


        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_operand)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.type_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.match(BKITParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.sub_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.array_id()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 416
                self.function_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 417
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_sub_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_expression" ):
                return visitor.visitSub_expression(self)
            else:
                return visitor.visitChildren(self)




    def sub_expression(self):

        localctx = BKITParser.Sub_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_sub_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(BKITParser.LB)
            self.state = 421
            self.expressions()
            self.state = 422
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def list_expression(self):
            return self.getTypedRuleContext(BKITParser.List_expressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(BKITParser.ID)
            self.state = 425
            self.match(BKITParser.LB)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 426
                self.list_expression()


            self.state = 429
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_list(self):
            return self.getTypedRuleContext(BKITParser.Type_listContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def list_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.List_expressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.List_expressionContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = BKITParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_list_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.type_list()
            self.state = 436
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 432
                    self.match(BKITParser.COMMA)
                    self.state = 433
                    self.list_expression() 
                self.state = 438
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = BKITParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(BKITParser.ID)
            self.state = 440
            self.match(BKITParser.LSB)
            self.state = 441
            self.expressions()
            self.state = 442
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[32] = self.exp1_sempred
        self._predicates[33] = self.exp2_sempred
        self._predicates[34] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




