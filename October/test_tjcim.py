""" Pytest file for October Challenge. """
import os
import csv
import logging
# from argparse import ArgumentError

import pytest

import tjcim


CSV_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), "csvs")


@pytest.fixture()
def a_list():
    """ Provide a list of lists for tests. """
    a_list_out = [
        ["John", "Doe", "120 jefferson st.", "Riverside", "NJ", "08075"],
        ["Jack", "McGinnis", "220 hobo Av.", "Phila", "PA", "09119"],
        ["John 'Da Man'", "Repici", "120 Jefferson St.", "Riverside", "NJ", "08075"],
        ["Stephen", "Tyler", "7452 Terrace 'At the Plaza' road", "SomeTown", "SD", "91234"],
        ["Joan 'the bone'", "Anne", "9th, at Terrace plc", "Desert City", "CO", "00123"],
    ]
    return a_list_out


@pytest.fixture()
def b_list():
    """ Provide a list of lists for tests. """
    b_list_out = [
        ["Month", "1958", "1959", "1960"],
        ["JAN", "340", "360", "417"],
        ["FEB", "318", "342", "391"],
        ["MAR", "362", "406", "419"],
        ["APR", "348", "396", "461"],
        ["MAY", "363", "420", "472"],
        ["JUN", "435", "472", "535"],
        ["JUL", "491", "548", "622"],
        ["AUG", "505", "559", "606"],
        ["SEP", "404", "463", "508"],
        ["OCT", "359", "407", "461"],
        ["NOV", "310", "362", "390"],
        ["DEC", "337", "405", "432"],
    ]
    return b_list_out


@pytest.fixture()
def a_file(tmpdir):
    """ Create a csv file to work with. """
    a_file = tmpdir.join('a_file.csv')  # pylint: disable=redefined-outer-name
    a_rows = [
        ["John", "Doe", "120 jefferson st.", "Riverside", "NJ", "08075"],
        ["Jack", "McGinnis", "220 hobo Av.", "Phila", "PA", "09119"],
        ["John 'Da Man'", "Repici", "120 Jefferson St.", "Riverside", "NJ", "08075"],
    ]

    with open(a_file.strpath, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(a_rows)

    return a_file


@pytest.fixture()
def b_file(tmpdir):
    """ Create b csv file to work with. """
    b_file = tmpdir.join('b_file.csv')  # pylint: disable=redefined-outer-name
    b_rows = [
        ["Stephen", "Tyler", "7452 Terrace 'At the Plaza' road", "SomeTown", "SD", "91234"],
        ["Joan 'the bone'", "Anne", "9th, at Terrace plc", "Desert City", "CO", "00123"],
    ]

    with open(b_file.strpath, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(b_rows)

    return b_file


def test_merge_all_files(a_file, b_file):  # pylint: disable=redefined-outer-name
    """ Test merging two csv files. """
    all_rows = [
        ["John", "Doe", "120 jefferson st.", "Riverside", "NJ", "08075"],
        ["Jack", "McGinnis", "220 hobo Av.", "Phila", "PA", "09119"],
        ["John 'Da Man'", "Repici", "120 Jefferson St.", "Riverside", "NJ", "08075"],
        ["Stephen", "Tyler", "7452 Terrace 'At the Plaza' road", "SomeTown", "SD", "91234"],
        ["Joan 'the bone'", "Anne", "9th, at Terrace plc", "Desert City", "CO", "00123"],
    ]
    assert all_rows == tjcim.merge_all_files([str(a_file), str(b_file)])


def test_write_list_to_csv(tmpdir):
    """ Tests the function write_list_to_csv. """
    all_rows = [
        ["John", "Doe", "120 jefferson st.", "Riverside", "NJ", "08075"],
        ["Jack", "McGinnis", "220 hobo Av.", "Phila", "PA", "09119"],
        ["John 'Da Man'", "Repici", "120 Jefferson St.", "Riverside", "NJ", "08075"],
        ["Stephen", "Tyler", "7452 Terrace 'At the Plaza' road", "SomeTown", "SD", "91234"],
        ["Joan 'the bone'", "Anne", "9th, at Terrace plc", "Desert City", "CO", "00123"],
    ]
    out_file = tmpdir.join('list_to_csv.csv')
    tjcim.write_list_to_csv(all_rows, out_file)
    # Assert file exists
    assert os.path.isfile(out_file)


def test_csv_to_list(a_file):  # pylint: disable=redefined-outer-name
    """ Tests the csv_to_list function. """
    a_rows = [
        ["John", "Doe", "120 jefferson st.", "Riverside", "NJ", "08075"],
        ["Jack", "McGinnis", "220 hobo Av.", "Phila", "PA", "09119"],
        ["John 'Da Man'", "Repici", "120 Jefferson St.", "Riverside", "NJ", "08075"],
    ]
    assert tjcim.csv_to_list(a_file) == a_rows
    with pytest.raises(SystemExit):
        tjcim.csv_to_list("file that does not exist")


class TestDownloadCSVFileToList:
    """ Tests for Download CSV File To List Function. """
    def test_valid_url(self):
        """ Tests the download download_csv_file_to_list function. """
        sample_csv_data = [
            ["Month", "1958", "1959", "1960"],
            ["JAN", "340", "360", "417"],
            ["FEB", "318", "342", "391"],
            ["MAR", "362", "406", "419"],
            ["APR", "348", "396", "461"],
            ["MAY", "363", "420", "472"],
            ["JUN", "435", "472", "535"],
            ["JUL", "491", "548", "622"],
            ["AUG", "505", "559", "606"],
            ["SEP", "404", "463", "508"],
            ["OCT", "359", "407", "461"],
            ["NOV", "310", "362", "390"],
            ["DEC", "337", "405", "432"],
        ]
        url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'
        assert sample_csv_data == tjcim.download_csv_file_to_list(url)

    def test_invalid_url(self):
        """ Test with invalid url. """
        url = 'http://.pystudygroup.com'
        with pytest.raises(SystemExit):
            tjcim.download_csv_file_to_list(url)


def test_get_line(a_list):  # pylint: disable=redefined-outer-name
    """ Test the get_line function. """
    expected = ["Jack", "McGinnis", "220 hobo Av.", "Phila", "PA", "09119"]
    results = tjcim.get_line(2, a_list)
    assert [expected] == results

    expected = ["Joan 'the bone'", "Anne", "9th, at Terrace plc", "Desert City", "CO", "00123"]
    results = tjcim.get_line(5, a_list)
    assert [expected] == results

    # invalid cases
    assert tjcim.get_line(20, a_list) is None
    assert tjcim.get_line(0, a_list) is None
    assert tjcim.get_line("a", a_list) is None


def test_remove_line(a_list, b_list):  # pylint: disable=redefined-outer-name
    """ Test the remove_line function. """
    expected = [
        ["Month", "1958", "1959", "1960"],
        ["JAN", "340", "360", "417"],
        ["FEB", "318", "342", "391"],
        ["MAR", "362", "406", "419"],
        ["MAY", "363", "420", "472"],
        ["JUN", "435", "472", "535"],
        ["JUL", "491", "548", "622"],
        ["AUG", "505", "559", "606"],
        ["SEP", "404", "463", "508"],
        ["OCT", "359", "407", "461"],
        ["NOV", "310", "362", "390"],
        ["DEC", "337", "405", "432"],
    ]
    results = tjcim.remove_line(5, b_list)
    assert expected == results

    expected = [
        ["Jack", "McGinnis", "220 hobo Av.", "Phila", "PA", "09119"],
        ["John 'Da Man'", "Repici", "120 Jefferson St.", "Riverside", "NJ", "08075"],
        ["Stephen", "Tyler", "7452 Terrace 'At the Plaza' road", "SomeTown", "SD", "91234"],
        ["Joan 'the bone'", "Anne", "9th, at Terrace plc", "Desert City", "CO", "00123"],
    ]
    results = tjcim.remove_line(1, a_list)
    assert expected == results

    # invalid cases
    assert tjcim.remove_line(20, b_list) is None
    assert tjcim.remove_line(0, b_list) is None
    assert tjcim.remove_line("a", b_list) is None


def test_filter_list(a_list, b_list):  # pylint: disable=redefined-outer-name
    """ Test the filter_list function. """
    # Test text
    expected = [
        ["John 'Da Man'", "Repici", "120 Jefferson St.", "Riverside", "NJ", "08075"],
    ]
    assert expected == tjcim.filter_list('Repici', a_list)

    # Test integer
    expected = [
        ["FEB", "318", "342", "391"],
    ]
    assert expected == tjcim.filter_list("342", b_list)

    # Test multiple
    expected = [
        ["MAY", "363", "420", "472"],
        ["JUN", "435", "472", "535"],
    ]
    assert expected == tjcim.filter_list("472", b_list)

    # invalid cases
    assert tjcim.filter_list("jjjj", a_list) is None


class TestParseArgs:
    """ Test parse args class """

    # Valid Tests
    @pytest.mark.parametrize("test_args, expected", [
        (
            ["--file", "blah.csv", "--filter", "342", "--output", "modified.blah.csv"],
            ("blah.csv", "342", "modified.blah.csv")
        ),
    ])
    def test_file_filter_output(self, test_args, expected):
        """ test parse args with valid file input, action, and output. """
        res = tjcim.parse_args(test_args)
        assert (res.file, res.filter, res.output_file) == expected

    @pytest.mark.parametrize("test_args, expected", [
        (
            ["--http-get-file", "http://www.google.com", "--get-line", "3", "--output",
             "modified.blah.csv"],
            ("http://www.google.com", 3, "modified.blah.csv")
        ),
    ])
    def test_http_get_line_output(self, test_args, expected):
        """ test parse args with valid http input, action, and output. """
        res = tjcim.parse_args(test_args)
        assert (res.http_get_file, res.get_line, res.output_file) == expected

    @pytest.mark.parametrize("test_args, expected", [
        (
            ["--merge", "blah1.csv", "blah2.csv", "blah3.csv", "--remove-line", "2", "--output",
             "modified_merge.csv"],
            (["blah1.csv", "blah2.csv", "blah3.csv"], 2, "modified_merge.csv")
        ),
    ])
    def test_merge_remove_line_output(self, test_args, expected):
        """ test parse args with valid merge input, action and output. """
        res = tjcim.parse_args(test_args)
        assert (res.merge, res.remove_line, res.output_file) == expected

    # Invalid Tests
    def test_merge_one_file(self):
        """ Merge called with one file should error. """
        with pytest.raises(SystemExit):
            tjcim.parse_args(["--merge", "blah1.csv"])

    def test_both_quiet_and_verbose(self):
        """ Called with both -v and -q. """
        with pytest.raises(SystemExit):
            tjcim.parse_args(["-v", "-q"])

    def test_two_inputs(self):
        """ Called with two inputs. """
        with pytest.raises(SystemExit):
            tjcim.parse_args(["--file", "blah.csv", "--http-get-file", "http://www.google.com"])

    def test_two_actions(self):
        """ Called with two actions. """
        with pytest.raises(SystemExit):
            tjcim.parse_args(["--get-line", "3", "--remove-line", "4"])

    def test_no_input(self):
        """ Called without an input. """
        with pytest.raises(SystemExit):
            tjcim.parse_args(["--filter", "fun", "output", "blah.fun.csv"])

    # Test logger
    def test_verbose(self):
        """ Test logger is set to DEBUG. """
        assert tjcim.log.isEnabledFor(logging.DEBUG) is False
        tjcim.parse_args(["--file", "blah.csv", "-v", "--remove-line", "3"])
        assert tjcim.log.isEnabledFor(logging.DEBUG) is True

    def test_quiet(self):
        """ Test logger is set to ERROR only. """
        assert tjcim.log.isEnabledFor(logging.WARN) is True
        tjcim.parse_args(["--file", "blah.csv", "-q", "--remove-line", "3"])
        assert tjcim.log.isEnabledFor(logging.WARN) is False
        assert tjcim.log.isEnabledFor(logging.ERROR) is True

    def test_info(self):
        """ Test that with no verbosity args the script remains at INFO. """
        tjcim.parse_args(["--file", "blah.csv", "--remove-line", "3"])
        assert tjcim.log.isEnabledFor(logging.INFO) is True


class TestMain:
    """ Test main function """
    def test_main_file(self, tmpdir):
        """ Test main with argument file """
        expected = [
            ['John', 'Doe', '120 jefferson st.', 'Riverside', 'NJ', '08075'],
            ['Jack', 'McGinnis', '220 hobo Av.', 'Phila', 'PA', '09119'],
            ['John "Da Man"', 'Repici', '120 Jefferson St.', 'Riverside', 'NJ', '08075'],
            ['', 'Blankman', '', 'SomeTown', 'SD', '00298'],
            ['Joan "the bone", Anne', 'Jet', '9th, at Terrace plc', 'Desert City', 'CO', '00123'],
        ]
        output_file = str(tmpdir.join("addresses_remove_line_4.csv"))
        args = tjcim.parse_args(["--file", os.path.join(CSV_FOLDER, "addresses.csv"),
                                 "--remove-line", "4", "--output-file",
                                 output_file])
        tjcim.main(args)
        assert os.path.isfile(output_file)
        assert tjcim.csv_to_list(output_file) == expected

    def test_main_http(self, tmpdir):
        """ Test main with argument http """
        expected = [
            ['Jack', 'McGinnis', '220 hobo Av.', 'Phila', 'PA', '09119'],
        ]
        output_file = str(tmpdir.join("http_get_line_2.csv"))
        args = tjcim.parse_args(["--http-get-file",
                                 "https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv",
                                 "--get-line", "2", "--output-file", output_file])
        tjcim.main(args)
        assert os.path.isfile(output_file)
        assert tjcim.csv_to_list(output_file) == expected

    def test_main_merge(self, tmpdir):
        """ Test main with merge. """
        expected = [
            ['John', 'Doe', '120 jefferson st.', 'Riverside', 'NJ', '08075'],
            ['John', 'M', '30', '68', '210'],
        ]
        output_file = str(tmpdir.join("merge_filter_John.csv"))
        args = tjcim.parse_args(["--merge",
                                 os.path.join(CSV_FOLDER, "addresses.csv"),
                                 os.path.join(CSV_FOLDER, "airtravel.csv"),
                                 os.path.join(CSV_FOLDER, "biostats.csv"),
                                 "--filter", "John", "--output-file", output_file])
        tjcim.main(args)
        assert os.path.isfile(output_file)
        assert tjcim.csv_to_list(output_file) == expected

    def test_main_no_action(self, tmpdir):
        """ Test main with no action. """
        expected = [
            ['John', 'Doe', '120 jefferson st.', 'Riverside', 'NJ', '08075'],
            ['Jack', 'McGinnis', '220 hobo Av.', 'Phila', 'PA', '09119'],
            ['John "Da Man"', 'Repici', '120 Jefferson St.', 'Riverside', 'NJ', '08075'],
            ['Stephen', 'Tyler', '7452 Terrace "At the Plaza" road', 'SomeTown', 'SD', '91234'],
            ['', 'Blankman', '', 'SomeTown', 'SD', '00298'],
            ['Joan "the bone", Anne', 'Jet', '9th, at Terrace plc', 'Desert City', 'CO', '00123'],
        ]
        output_file = str(tmpdir.join("no_action.csv"))
        args = tjcim.parse_args(["--file", os.path.join(CSV_FOLDER, "addresses.csv"),
                                 "--output-file", output_file])
        tjcim.main(args)
        assert os.path.isfile(output_file)
        assert tjcim.csv_to_list(output_file) == expected
