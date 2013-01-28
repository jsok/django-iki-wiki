from unittest import TestCase, main

from utils import title_from_slug

class PageTitleTestCase(TestCase):
    def test_title_from_slug(self):
        # Input, Output tuples
        tests = [
            ("Foo", "Foo"),
            ("human_body", "Human Body"),
            ("HumanBody", "Human Body"),
            ("Parts_of_the_HumanBody", "Parts Of The Human Body"),
            ("HumanBody/Parts", "Human Body / Parts"),
        ]

        for input, expected_output in tests:
            output = title_from_slug(input)
            self.assertEqual(expected_output, output,
                "{input} title produced {output} instead of {expected_output}".format(
                    input=input, output=output, expected_output=expected_output
                )
            )

if __name__ == '__main__':
    main()