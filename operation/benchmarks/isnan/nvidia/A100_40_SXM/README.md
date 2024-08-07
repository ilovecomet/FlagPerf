# 参评AI芯片信息

* 厂商：Nvidia


* 产品名称：A100
* 产品型号：A100-40GiB-SXM
* TDP：400W

# 所用服务器配置

* 服务器数量：1


* 单服务器内使用卡数：1
* 服务器型号：DGX A100
* 操作系统版本：Ubuntu 20.04.4 LTS
* 操作系统内核：linux5.4.0-113
* CPU：AMD EPYC7742-64core
* docker版本：20.10.16
* 内存：1TiB
* 服务器间AI芯片直连规格及带宽：此评测项不涉及服务期间AI芯片直连

# 算子库版本

https://github.com/FlagOpen/FlagGems. Commit ID:1e49d6bf2cc50dee133a9a70a1e90851668be931

# 评测结果

## 核心评测结果

| 评测项  | 平均相对误差(with FP64-CPU) | TFLOPS(cpu wall clock) | TFLOPS(kernel clock) | FU(FLOPS Utilization)-cputime | FU-kerneltime |
| ---- | -------------- | -------------- | ------------ | ------ | ----- |
| flaggems | 0.00E+00    | 0.28TFLOPS       | 0.27TFLOPS        | 1.42% | 1.41% |
| nativetorch | 0.00E+00    | 0.28TFLOPS      | 0.28TFLOPS      | 1.43%      | 1.43%    |

## 其他评测结果

| 评测项  | 相对误差(with FP64-CPU)标准差 | cputime | kerneltime | cputime吞吐 | kerneltime吞吐 | 无预热时延 | 预热后时延 |
| ---- | -------------- | -------------- | ------------ | ------------ | -------------- | -------------- | ------------ |
| flaggems | 0.00E+00    | 3887.65us       | 3907.58us        | 257.23op/s | 255.91op/s | 912492.7us | 3971.57us |
| nativetorch | 0.00E+00    | 3841.77us       | 3856.38us        | 260.3op/s | 259.31op/s | 5746.19us | 3871.9us |

## 能耗监控结果

| 监控项  | 系统平均功耗  | 系统最大功耗  | 系统功耗标准差 | 单机TDP | 单卡平均功耗 | 单卡最大功耗 | 单卡功耗标准差 | 单卡TDP |
| ---- | ------- | ------- | ------- | ----- | ------------ | ------------ | ------------- | ----- |
| nativetorch监控结果 | 1521.0W | 1638.0W | 117.0W   | /     | 265.49W       | 272.0W      | 3.23W        | 1521.0  |
| flaggems监控结果 | 1521.0W | 1638.0W | 117.0W   | /     | 251.77W       | 256.0W      | 2.63W        | 1521.0  |

## 其他重要监控结果

| 监控项  | 系统平均CPU占用 | 系统平均内存占用 | 单卡平均温度 | 单卡最大显存占用 |
| ---- | --------- | -------- | ------------ | -------------- |
| nativetorch监控结果 | 0.579%    | 1.796%   | 48.51°C       | 16.378%        |
| flaggems监控结果 | 0.566%    | 1.8%   | 47.38°C       | 16.195%        |
