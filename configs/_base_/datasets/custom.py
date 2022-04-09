dataset_info = dict(
    dataset_name='excavator_2D',
    paper_info=dict(
        author='Luo, Han'
        'Wang, Mingzhu'
        'Wong, Peter Kok-Yiu'
        'Cheng, Jack C. P.',
        title='Full body pose estimation of construction equipment using computer vision and deep learning techniques',
        container='Automation in Construction',
        year='2020',
        homepage='https://hkustbimlab.github.io',
    ),
    keypoint_info={
        0:
        dict(name='body_end', id=0, color=[255, 0, 0], swap=''),
        1:
        dict(
            name='cab_boom',
            id=1,
            color=[0, 255, 0],
            swap=''),
        2:
        dict(
            name='boom_arm',
            id=2,
            color=[0, 0, 255],
            swap=''),
        3:
        dict(
            name='arm_bucket',
            id=3,
            color=[255, 0, 255],
            type='upper',
            swap='right_ear'),
        4:
        dict(
            name='bucket_end_left',
            id=4,
            color=[255, 255, 0],
            swap='bucket_end_right'),
        5:
        dict(
            name='bucket_end_right',
            id=5,
            color=[0, 255, 255],
            swap='bucket_end_left')
    },
    skeleton_info={
        0:
        dict(link=('body_end', 'cab_boom'), id=0, color=[51, 153, 255]),
        1:
        dict(link=('cab_boom', 'boom_arm'), id=1, color=[0, 255, 0]),
        2:
        dict(link=('boom_arm', 'arm_bucket'), id=2, color=[255, 128, 0]),
        3:
        dict(link=('arm_bucket', 'bucket_end_right'), id=3, color=[255, 128, 0]),
        4:
        dict(link=('bucket_end_right', 'bucket_end_left'), id=4, color=[51, 153, 255]),
        5:
        dict(link=('bucket_end_left', 'arm_bucket'), id=5, color=[51, 153, 255]),
    },
    joint_weights=[
        1., 1., 1., 1., 1., 1.
    ],
    sigmas=[
        0.，0.，0.，0.，0.，0.
    ])