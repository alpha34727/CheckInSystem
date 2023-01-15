
# 線上出缺勤管理系統

## 使用者角色
- 組織管理員
- 組織成員
- 訪客

## 網站功能架構

### 組織成員（需登入）：
- 登出
- 變更密碼
- 打卡
- 申請請假
- 檢視自身出缺勤紀錄

### 訪客（不需登入）：
- 登入系統
- 註冊帳號

## 資料定義

### 使用者資訊(`django.contrib.auth`)
- **使用者名稱**
單行文字

- **密碼**
單行文字

### 組織成員
- **使用者id**
整數

- **是否打過卡**
布林

- **開始打卡時間**
日期時間欄位

### 請假(補假)申請、紀錄
- **使用者id**
整數

- **開始時間**
日期時間欄位

- **結束時間**
日期時間欄位

- **資訊**
單行文字

- **是否審核**
布林

### 出缺勤紀錄
- **使用者id**
整數

- **開始時間**
日期時間欄位

- **結束時間**
日期時間欄位

- **資訊**
單行文字
