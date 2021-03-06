import hashlib
import unittest
import yaml

import w266_common.answers_helper as ah

class AnswersTest(unittest.TestCase):
    REQUIRED_ANSWERS = ['info_a1', 'info_a2', 'info_a2_speculation', 'info_b1_1_128msg_num_bits', 'info_b1_2_128msg_entropy', 'info_b1_3_1024msg_num_bits', 'info_b2', 'info_b3', 'info_c1', 'info_c2_1', 'info_c2_2', 'info_c3', 'info_c4', 'info_c5', 'info_c6', 'dp_a1', 'dp_a2', 'dp_a3', 'dp_b1_A', 'dp_b1_B', 'dp_b1_C', 'dp_b2', 'dp_b3', 'dp_c1', 'dp_c2', 'dp_c3', 'dp_c4', 'dp_d_helloworldhowareyou', 'dp_d_downbythebay', 'dp_d_wikipediaisareallystrongresourceontheinternet', 'dp_e1', 'dp_e2', 'dp_e3', 'dp_e4', 'tf_b_W_shape', 'tf_b_b_shape', 'tf_c_W_shape', 'tf_c_b_shape', 'tf_c_x_shape', 'tf_c_z_shape', 'tf_d_y_hat_shape', 'tf_d_y_hat_tensor', 'tf_d_elementwise_description', 'tf_e_W_shape', 'tf_e_b_shape', 'tf_e_x_shape', 'tf_e_z_shape']

    FLOAT_ANSWERS = ['dp_a1', 'dp_b1_A', 'dp_b1_B', 'dp_b1_C', 'dp_b3', 'dp_e3', 'info_a1', 'info_a2', 'info_b1_1_128msg_num_bits', 'info_b1_2_128msg_entropy', 'info_b1_3_1024msg_num_bits', 'info_c1', 'info_c2_1', 'info_c4']

    def setUp(self):
        with open('answers', 'r') as f:
            self.answers = yaml.safe_load(f.read())

    def test_keys(self):
        self.assertEqual(
                sorted(AnswersTest.REQUIRED_ANSWERS),
                sorted(self.answers.keys()))

    def test_shape_answers(self):
      for k, v in sorted(self.answers.items()):
        if k.endswith('_shape') or k.endswith('_tensor'):
          self.assertTrue(ah.parse_shape(v), msg='Bad shape format for %s' % k)

    def test_float_answers(self):
      for k, v in sorted(self.answers.items()):
        if k in AnswersTest.FLOAT_ANSWERS:
          try:
            float(v)
          except:
            self.fail(msg='%s should be a float, but is not (%s)' % (k, v)) 

if __name__ == '__main__':
    unittest.main()

