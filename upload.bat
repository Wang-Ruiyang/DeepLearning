@echo off
 
title wry/leetcode-java�Զ��ύ��

color 2
echo ��ǰĿ¼�ǣ�%cd%
echo;

echo ��ʼ��ӱ����git add .
git add .
echo;

set /p declation=�����ύ��commit��Ϣ��
git commit -m "%declation%"
echo;
 
echo �����ϴ�Զ������֧
git push
echo;
 
echo ִ����ϣ�
echo;
 
pause