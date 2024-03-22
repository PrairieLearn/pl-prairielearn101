
from pl_helpers import name, points, not_repeated
from code_feedback import Feedback
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
import json
import math

class Test(PLTestCaseWithPlot):
    
  def verify(self, function_name, expected, params_json):
    params = json.loads(params_json)
    observed = Feedback.call_user(getattr(self.st, function_name), *params)
    msg = f"'{function_name}({params_json})' did not return {expected} as expected. It returned {observed}."
   
    float_close = isinstance(expected, float) and math.isclose(expected, observed) 
    is_equal = (not isinstance(expected, float) and expected == observed)

    if (float_close or is_equal):
      Feedback.set_score(1)
    else:
      Feedback.add_feedback(msg)
      Feedback.set_score(0)

  student_code_file = 'learning_target.ipynb'

  # Make sure there is a newline here->

  
  @points(1)
  @name("test 1")
  def test_01(self):
      self.verify('dict_bully', {'a': '<stolen>', 'b': 'candy'}, '[{"a": "candy", "b": "dirt"}]')

  @points(1)
  @name("test 2")
  def test_02(self):
      self.verify('dict_bully', {'a': '<stolen>', 'b': 'candy'}, '[{"a": "candy"}]')

  @points(1)
  @name("test 3")
  def test_03(self):
      self.verify('dict_bully', {'a': '<stolen>', 'b': 'candy', 'c': 'meh'}, '[{"a": "candy", "b": "carrot", "c": "meh"}]')

  @points(1)
  @name("test 4")
  def test_04(self):
      self.verify('dict_bully', {'a': '<stolen>', 'b': 'candy'}, '[{"a": "candy", "b": "dirt"}]')

  @points(1)
  @name("test 5")
  def test_05(self):
      self.verify('dict_bully', {'a': '<stolen>', 'b': 'candy'}, '[{"a": "candy"}]')

  @points(1)
  @name("test 6")
  def test_06(self):
      self.verify('dict_bully', {'a': '<stolen>', 'b': 'candy', 'c': 'meh'}, '[{"a": "candy", "b": "carrot", "c": "meh"}]')

  @points(1)
  @name("test 7")
  def test_07(self):
      self.verify('dict_bully', {'b': 'carrot'}, '[{"b": "carrot"}]')

  @points(1)
  @name("test 8")
  def test_08(self):
      self.verify('dict_bully', {'c': 'meh'}, '[{"c": "meh"}]')

  @points(1)
  @name("test 9")
  def test_09(self):
      self.verify('dict_bully', {'a': '<stolen>', 'b': 'sparkle', 'c': 'meh'}, '[{"a": "sparkle", "c": "meh"}]')

  @points(1)
  @name("test 10")
  def test_10(self):
      self.verify('dict_AB', {'a': 'Hi', 'ab': 'HiThere', 'b': 'There'}, '[{"a": "Hi", "b": "There"}]')

  @points(1)
  @name("test 11")
  def test_11(self):
      self.verify('dict_AB', {'a': 'Hi'}, '[{"a": "Hi"}]')

  @points(1)
  @name("test 12")
  def test_12(self):
      self.verify('dict_AB', {'b': 'There'}, '[{"b": "There"}]')

  @points(1)
  @name("test 13")
  def test_13(self):
      self.verify('dict_AB', {'a': 'Hi', 'ab': 'HiThere', 'b': 'There'}, '[{"a": "Hi", "b": "There"}]')

  @points(1)
  @name("test 14")
  def test_14(self):
      self.verify('dict_AB', {'a': 'Hi'}, '[{"a": "Hi"}]')

  @points(1)
  @name("test 15")
  def test_15(self):
      self.verify('dict_AB', {'b': 'There'}, '[{"b": "There"}]')

  @points(1)
  @name("test 16")
  def test_16(self):
      self.verify('dict_AB', {'c': 'meh'}, '[{"c": "meh"}]')

  @points(1)
  @name("test 17")
  def test_17(self):
      self.verify('dict_AB', {'a': 'aaa', 'ab': 'aaabbb', 'b': 'bbb', 'c': 'ccc'}, '[{"a": "aaa", "ab": "nope", "b": "bbb", "c": "ccc"}]')

  @points(1)
  @name("test 18")
  def test_18(self):
      self.verify('dict_AB', {'ab': 'nope', 'b': 'bbb', 'c': 'ccc'}, '[{"ab": "nope", "b": "bbb", "c": "ccc"}]')

  @points(1)
  @name("test 19")
  def test_19(self):
      self.verify('topping_1', {'bread': 'butter', 'ice cream': 'cherry'}, '[{"ice cream": "peanuts"}]')

  @points(1)
  @name("test 20")
  def test_20(self):
      self.verify('topping_1', {'bread': 'butter'}, '[{}]')

  @points(1)
  @name("test 21")
  def test_21(self):
      self.verify('topping_1', {'bread': 'butter', 'pancake': 'syrup'}, '[{"pancake": "syrup"}]')

  @points(1)
  @name("test 22")
  def test_22(self):
      self.verify('topping_1', {'bread': 'butter', 'ice cream': 'cherry'}, '[{"ice cream": "peanuts"}]')

  @points(1)
  @name("test 23")
  def test_23(self):
      self.verify('topping_1', {'bread': 'butter'}, '[{}]')

  @points(1)
  @name("test 24")
  def test_24(self):
      self.verify('topping_1', {'bread': 'butter', 'pancake': 'syrup'}, '[{"pancake": "syrup"}]')

  @points(1)
  @name("test 25")
  def test_25(self):
      self.verify('topping_1', {'bread': 'butter', 'ice cream': 'cherry'}, '[{"bread": "dirt", "ice cream": "strawberries"}]')

  @points(1)
  @name("test 26")
  def test_26(self):
      self.verify('topping_1', {'bread': 'butter', 'ice cream': 'cherry', 'salad': 'oil'}, '[{"bread": "jam", "ice cream": "strawberries", "salad": "oil"}]')

  @points(1)
  @name("test 27")
  def test_27(self):
      self.verify('topping_2', {'yogurt': 'cherry', 'ice cream': 'cherry'}, '[{"ice cream": "cherry"}]')

  @points(1)
  @name("test 28")
  def test_28(self):
      self.verify('topping_2', {'yogurt': 'cherry', 'spinach': 'nuts', 'ice cream': 'cherry'}, '[{"spinach": "dirt", "ice cream": "cherry"}]')

  @points(1)
  @name("test 29")
  def test_29(self):
      self.verify('topping_2', {'yogurt': 'salt'}, '[{"yogurt": "salt"}]')

  @points(1)
  @name("test 30")
  def test_30(self):
      self.verify('topping_2', {'yogurt': 'cherry', 'ice cream': 'cherry'}, '[{"ice cream": "cherry"}]')

  @points(1)
  @name("test 31")
  def test_31(self):
      self.verify('topping_2', {'yogurt': 'cherry', 'spinach': 'nuts', 'ice cream': 'cherry'}, '[{"spinach": "dirt", "ice cream": "cherry"}]')

  @points(1)
  @name("test 32")
  def test_32(self):
      self.verify('topping_2', {'yogurt': 'salt'}, '[{"yogurt": "salt"}]')

  @points(1)
  @name("test 33")
  def test_33(self):
      self.verify('topping_2', {'yogurt': 'salt', 'bread': 'butter'}, '[{"yogurt": "salt", "bread": "butter"}]')

  @points(1)
  @name("test 34")
  def test_34(self):
      self.verify('topping_2', {}, '[{}]')

  @points(1)
  @name("test 35")
  def test_35(self):
      self.verify('topping_2', {'yogurt': 'air', 'ice cream': 'air', 'salad': 'oil'}, '[{"ice cream": "air", "salad": "oil"}]')

  @points(1)
  @name("test 36")
  def test_36(self):
      self.verify('dict_AB2', {'c': 'cake'}, '[{"a": "aaa", "b": "aaa", "c": "cake"}]')

  @points(1)
  @name("test 37")
  def test_37(self):
      self.verify('dict_AB2', {'a': 'aaa', 'b': 'bbb'}, '[{"a": "aaa", "b": "bbb"}]')

  @points(1)
  @name("test 38")
  def test_38(self):
      self.verify('dict_AB2', {'a': 'aaa', 'b': 'bbb', 'c': 'aaa'}, '[{"a": "aaa", "b": "bbb", "c": "aaa"}]')

  @points(1)
  @name("test 39")
  def test_39(self):
      self.verify('dict_AB2', {'c': 'cake'}, '[{"a": "aaa", "b": "aaa", "c": "cake"}]')

  @points(1)
  @name("test 40")
  def test_40(self):
      self.verify('dict_AB2', {'a': 'aaa', 'b': 'bbb'}, '[{"a": "aaa", "b": "bbb"}]')

  @points(1)
  @name("test 41")
  def test_41(self):
      self.verify('dict_AB2', {'a': 'aaa', 'b': 'bbb', 'c': 'aaa'}, '[{"a": "aaa", "b": "bbb", "c": "aaa"}]')

  @points(1)
  @name("test 42")
  def test_42(self):
      self.verify('dict_AB2', {'a': 'aaa'}, '[{"a": "aaa"}]')

  @points(1)
  @name("test 43")
  def test_43(self):
      self.verify('dict_AB2', {'b': 'bbb'}, '[{"b": "bbb"}]')

  @points(1)
  @name("test 44")
  def test_44(self):
      self.verify('dict_AB2', {'c': 'ccc'}, '[{"a": "", "b": "", "c": "ccc"}]')

  @points(1)
  @name("test 45")
  def test_45(self):
      self.verify('dict_AB2', {}, '[{}]')

  @points(1)
  @name("test 46")
  def test_46(self):
      self.verify('dict_AB2', {'a': 'a', 'b': 'b', 'z': 'zebra'}, '[{"a": "a", "b": "b", "z": "zebra"}]')

  @points(1)
  @name("test 47")
  def test_47(self):
      self.verify('dict_AB3', {'a': 'aaa', 'b': 'aaa', 'c': 'cake'}, '[{"a": "aaa", "c": "cake"}]')

  @points(1)
  @name("test 48")
  def test_48(self):
      self.verify('dict_AB3', {'a': 'bbb', 'b': 'bbb', 'c': 'cake'}, '[{"b": "bbb", "c": "cake"}]')

  @points(1)
  @name("test 49")
  def test_49(self):
      self.verify('dict_AB3', {'a': 'aaa', 'b': 'bbb', 'c': 'cake'}, '[{"a": "aaa", "b": "bbb", "c": "cake"}]')

  @points(1)
  @name("test 50")
  def test_50(self):
      self.verify('dict_AB3', {'a': 'aaa', 'b': 'aaa', 'c': 'cake'}, '[{"a": "aaa", "c": "cake"}]')

  @points(1)
  @name("test 51")
  def test_51(self):
      self.verify('dict_AB3', {'a': 'bbb', 'b': 'bbb', 'c': 'cake'}, '[{"b": "bbb", "c": "cake"}]')

  @points(1)
  @name("test 52")
  def test_52(self):
      self.verify('dict_AB3', {'a': 'aaa', 'b': 'bbb', 'c': 'cake'}, '[{"a": "aaa", "b": "bbb", "c": "cake"}]')

  @points(1)
  @name("test 53")
  def test_53(self):
      self.verify('dict_AB3', {'ccc': 'ccc'}, '[{"ccc": "ccc"}]')

  @points(1)
  @name("test 54")
  def test_54(self):
      self.verify('dict_AB3', {'c': 'a', 'd': 'b'}, '[{"c": "a", "d": "b"}]')

  @points(1)
  @name("test 55")
  def test_55(self):
      self.verify('dict_AB3', {}, '[{}]')

  @points(1)
  @name("test 56")
  def test_56(self):
      self.verify('dict_AB3', {'a': '', 'b': ''}, '[{"a": ""}]')

  @points(1)
  @name("test 57")
  def test_57(self):
      self.verify('dict_AB3', {'a': '', 'b': ''}, '[{"b": ""}]')

  @points(1)
  @name("test 58")
  def test_58(self):
      self.verify('dict_AB3', {'a': '', 'b': ''}, '[{"a": "", "b": ""}]')

  @points(1)
  @name("test 59")
  def test_59(self):
      self.verify('dict_AB3', {'aa': 'aa', 'a': 'apple', 'b': 'apple', 'z': 'zzz'}, '[{"aa": "aa", "a": "apple", "z": "zzz"}]')

  @points(1)
  @name("test 60")
  def test_60(self):
      self.verify('dict_AB4', {'a': 'aaa', 'b': 'bb', 'c': 'aaa'}, '[{"a": "aaa", "b": "bb", "c": "cake"}]')

  @points(1)
  @name("test 61")
  def test_61(self):
      self.verify('dict_AB4', {'a': 'aa', 'b': 'bbb', 'c': 'bbb'}, '[{"a": "aa", "b": "bbb", "c": "cake"}]')

  @points(1)
  @name("test 62")
  def test_62(self):
      self.verify('dict_AB4', {'a': 'aa', 'b': 'bbb', 'c': 'bbb'}, '[{"a": "aa", "b": "bbb"}]')

  @points(1)
  @name("test 63")
  def test_63(self):
      self.verify('dict_AB4', {'a': 'aaa', 'b': 'bb', 'c': 'aaa'}, '[{"a": "aaa", "b": "bb", "c": "cake"}]')

  @points(1)
  @name("test 64")
  def test_64(self):
      self.verify('dict_AB4', {'a': 'aa', 'b': 'bbb', 'c': 'bbb'}, '[{"a": "aa", "b": "bbb", "c": "cake"}]')

  @points(1)
  @name("test 65")
  def test_65(self):
      self.verify('dict_AB4', {'a': 'aa', 'b': 'bbb', 'c': 'bbb'}, '[{"a": "aa", "b": "bbb"}]')

  @points(1)
  @name("test 66")
  def test_66(self):
      self.verify('dict_AB4', {'a': 'aaa'}, '[{"a": "aaa"}]')

  @points(1)
  @name("test 67")
  def test_67(self):
      self.verify('dict_AB4', {'b': 'bbb'}, '[{"b": "bbb"}]')

  @points(1)
  @name("test 68")
  def test_68(self):
      self.verify('dict_AB4', {'a': '', 'b': '', 'c': 'cake'}, '[{"a": "aaa", "b": "bbb", "c": "cake"}]')

  @points(1)
  @name("test 69")
  def test_69(self):
      self.verify('dict_AB4', {'a': '', 'b': '', 'c': 'cake'}, '[{"a": "a", "b": "b", "c": "cake"}]')

  @points(1)
  @name("test 70")
  def test_70(self):
      self.verify('dict_AB4', {'a': '', 'b': 'b', 'c': 'b'}, '[{"a": "", "b": "b", "c": "cake"}]')

  @points(1)
  @name("test 71")
  def test_71(self):
      self.verify('dict_AB4', {'a': 'a', 'b': '', 'c': 'a'}, '[{"a": "a", "b": "", "c": "cake"}]')

  @points(1)
  @name("test 72")
  def test_72(self):
      self.verify('dict_AB4', {'c': 'cat', 'd': 'dog'}, '[{"c": "cat", "d": "dog"}]')

  @points(1)
  @name("test 73")
  def test_73(self):
      self.verify('dict_AB4', {'ccc': 'ccc'}, '[{"ccc": "ccc"}]')

  @points(1)
  @name("test 74")
  def test_74(self):
      self.verify('dict_AB4', {'c': 'a', 'd': 'b'}, '[{"c": "a", "d": "b"}]')

  @points(1)
  @name("test 75")
  def test_75(self):
      self.verify('dict_AB4', {}, '[{}]')

  @points(1)
  @name("test 76")
  def test_76(self):
      self.verify('dict_AB4', {'a': '', 'z': 'z'}, '[{"a": "", "z": "z"}]')

  @points(1)
  @name("test 77")
  def test_77(self):
      self.verify('dict_AB4', {'b': '', 'z': 'z'}, '[{"b": "", "z": "z"}]')

