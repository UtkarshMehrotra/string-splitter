from tag_manipulator import TagManipulator

def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_one_string_result_array_of_one():
    # arrange
    stringToSplit = "java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_one_string_result_array_of_two():
    # arrange
    stringToSplit = "java,python"
    regex = ","
    expResult = ["java","python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_one_string_result_array_of_two_with_white_space():
    # arrange
    stringToSplit = " java, python "
    regex = ","
    expResult = ["java","python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_one_string_comma_first():
    # arrange
    stringToSplit = ",java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_one_string_multiple_strings_multiple_commas():
    # arrange
    stringToSplit = ",java ,, python, ££ , C++"
    regex = ","
    expResult = ["java","python","££","C++"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_one_string_comma_at_the_end():
    # arrange
    stringToSplit = "java,"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_multiple_strings_multiple_special_characters():
    # arrange
    stringToSplit = "java$$,python//,C++,BASH"
    regex = ","
    expResult = ["java$$","python//","C++","BASH"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult