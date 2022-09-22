import maya.cmds as cmds


def core(percentage, obj=None, attrs=None, selection=True):
	"""
	This function will tween the keyed attributes on any given object
	Args:
		percentage: float - This is a madatory arg and will be the percentage being tweened
		obj: string - The name of the object to use, it's optional since it has a default value
		attrs: list - A listof attributes to tween, also option since we are suppling a default value
		selection: bool - Whether to use the selection of not, also optional because we are suppling a default value
	"""

	# Check for obj and selection if neither then raise error
	if not obj and not selection:
		raise ValueError("No object to tween")

	# Check for object existance and cast into obj var
	if not obj:
		obj = cmds.ls(sl=1)[0]

	# Cast all keyable attributes off object selection
	if not attrs:
		attrs = cmds.listAttr(obj, keyable=True)

	# Capture current time frame
	currentTime = cmds.currentTime(query=True)

	# We have all we need let's loop through the attrs
	for attr in attrs:
		attrFull = '{}.{}'.format(obj, attr)
		keyframes = cmds.keyframe(attrFull, query=True)

		# If there are no keyframes, then it isn't keyed and we can skip it
		if not keyframes:
			continue

		# Create and empty list to hold the values of our previous keyframes and append to
		previousKeyframes = []
		for k in keyframes:
			if k < currentTime:
				previousKeyframes.append(k)

		# Our List Comprehension checking if the keyframes are greater that the currentTime
		laterKeyframes = [frame for frame in keyframes if frame > currentTime]

		# If we don't have either previous or later frames then skip ahead
		if not previousKeyframes and not laterKeyframes:
			continue

		# If we do have previous frames, we need the nearest one otherwise set to None
		if previousKeyframes:
			previousFrame = max(previousKeyframes)
		else:
			previousFrame = None

		# If we have a next frame, we need to grab the nearest on or set to None
		nextFrame = min(laterKeyframes) if laterKeyframes else None

		# If we don't find previous frame, set to nextFrame to help our logic further down
		if previousFrame is None:
			previousFrame = nextFrame

		# If we don't find next frame, set to previousFrame to help our logic further down
		nextFrame = previousFrame if nextFrame is None else nextFrame

		# Query the values of the attributes on the current frame 
		previousValue = cmds.getAttr(attrFull, time=previousFrame)
		nextValue = cmds.getAttr(attrFull, time=nextFrame)

		# If there are no nextFrames, or PreviousFrames set the values to the closest previous or next frame 
		# Or they are both equal then set the value to the previous, Else if they are different calculate the tweening value
		if nextFrame is None:
			currentValue = previousValue
		
		elif previousFrame is None:
			currentValue = nextValue
		
		elif previousValue == nextValue:
			currentValue = previousValue
		
		else:
			difference = nextValue - previousValue
			biasedDifference = (difference * percentage) / 100.0
			currentValue = previousValue + biasedDifference

		# We need to set the current value of the attrFull and set the keyframe
		cmds.setAttr(attrFull, currentValue)
		cmds.setKeyframe(attrFull, time=currentTime, value=currentValue)



