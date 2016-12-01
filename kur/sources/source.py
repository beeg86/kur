"""
Copyright 2016 Deepgram

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

###############################################################################
class Source:						# pylint: disable=too-few-public-methods
	""" Base class for all data sources.

		Data sources are responsible for producing data that will be presented
		to the model for training, validation, or prediction (evaluation).

		Each data source provides one of the input or output tensors that the
		network needs.
	"""

	###########################################################################
	def __init__(self):
		""" Create a new data source.
		"""
		pass

	###########################################################################
	def __iter__(self):
		""" Return an iterator to the data.

			The iterator should return a tensor of shape `(X, ) +
			self.shape()`, where `X` is the number of entries provided by this
			data source.
		"""
		raise NotImplementedError

	###########################################################################
	def __len__(self):
		""" Returns the total number of entries that this source can return, if
			known.

			# Return value

			If the total number of entries that this source can return is
			known, it should be returned. In the simplest case, this is the
			same as the number of training samples in an epoch. If this number
			is unknown or effectively infinite (because it is from some
			real-time data generator or is being streamed from some
			uncontrolled source, for example), then this should return None.
		"""
		raise NotImplementedError

	###########################################################################
	def shape(self):
		""" Return the shape of the tensor (excluding batch size) returned by
			this data source.

			# Return value

			A shape tuple (length of each dimension in the tensor).
		"""
		raise NotImplementedError

### EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF
