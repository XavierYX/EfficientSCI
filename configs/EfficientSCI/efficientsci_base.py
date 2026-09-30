_base_=[
        "../_base_/six_gray_sim_data.py",
        "../_base_/davis.py",
        "../_base_/default_runtime.py"
        ]

data = dict(
    samples_per_gpu=1,
    workers_per_gpu=4,
)

resize_h,resize_w = 256,256
train_pipeline = [ 
    dict(type='RandomResize'),
    dict(type='RandomCrop',crop_h=resize_h,crop_w=resize_w,random_size=True),
    dict(type='Flip', direction='horizontal',flip_ratio=0.5,),
    dict(type='Flip', direction='diagonal',flip_ratio=0.5,),
    dict(type='Resize', resize_h=resize_h,resize_w=resize_w),
]
train_data = dict(
    mask_path = None,
    mask_shape = (resize_h,resize_w,8),
    pipeline = train_pipeline
)
test_data = dict(
    data_root="test_datasets/simulation/article",
    mask_path="test_datasets/mask/real_mask_cr8_sim.mat"
)
real_data = dict(
    type="GrayRealData",
    mask_path="test_datasets/mask/real_mask_cr8_WF.mat",
    cr=8,
    data_root="test_datasets/real_data/cr8/WF"
)
model = dict(
    type='EfficientSCI',
    in_ch=64, 
    units=8,
    group_num=4,
    color_ch=1
)

eval=dict(
    flag=True,
    interval=1
)

checkpoints="checkpoints/efficientsci_finetune.pth"