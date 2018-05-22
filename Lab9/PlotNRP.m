M = csvread('joint_states (2).csv',2,1);

plot(M(:,1),M(:,2));
hold on;
yyaxis right
plot(M(:,1),M(:,3));
grid on;

figure;
plot(M(:,2),M(:,3));
grid on
