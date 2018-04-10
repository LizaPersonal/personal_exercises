from nose.tools import *
from ..ex48 import parser


def test_peek():
    assert_equal(parser.peek([('direction', 'north')]), 'direction')
    result = parser.peek([('noun', 'ball'),
                          ('verb', 'throw')])
    assert_equal(result, 'noun')


def test_match():
    assert_equal(parser.match([('direction', 'north')], 'direction'), ('direction', 'north'))
    result = parser.match([('noun', 'ball'),
                          ('verb', 'throw')], 'noun')
    assert_equal(result, ('noun', 'ball'))
    assert_equal(parser.match([('stop', 'the')], 'noun'), None)


def test_skip():
    pass


def test_parse_verb():
    assert_equal(parser.parse_verb([('verb', 'jump')]), ('verb', 'jump'))
    result = parser.parse_verb([('stop', 'the'),
                                ('verb', 'throw')])
    assert_equal(result, ('verb', 'throw'))
    # assert_raises(parser.ParserError("Expected a verb next."), parser.parse_verb([('noun', 'cat')]))


def test_parse_object():
    assert_equal(parser.parse_object([('noun', 'building')]), ('noun', 'building'))
    assert_equal(parser.parse_object([('direction', 'west')]), ('direction', 'west'))
    result = parser.parse_object([('stop', 'the'),
                                ('noun', 'chair')])
    assert_equal(result, ('noun', 'chair'))


def test_parse_subject():
    assert_equal(parser.parse_subject([('noun', 'hair')]), ('noun', 'hair'))
    assert_equal(parser.parse_subject([('verb', 'run')]), ('noun', 'player'))
    result = parser.parse_subject([('stop', 'the'),
                                  ('noun', 'tree')])
    assert_equal(result, ('noun', 'tree'))


def test_parse_sentence():
    result = parser.parse_sentence([('stop', 'the'),
                                    ('noun', 'boy'),
                                    ('verb', 'ran'),
                                    ('stop', 'to'),
                                    ('noun', 'town')])
    assert_equal(result.subject, 'boy')
    assert_equal(result.verb, 'ran')
    assert_equal(result.object, 'town')
    result = parser.parse_sentence([('verb', 'walks'),
                                    ('direction', 'left')])
    assert_equal(result.subject, 'player')
    assert_equal(result.verb, 'walks')
    assert_equal(result.object, 'left')


def test_errors():
    pass