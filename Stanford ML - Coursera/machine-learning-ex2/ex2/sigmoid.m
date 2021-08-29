function g = sigmoid(z)
%SIGMOID Compute sigmoid function
%   g = SIGMOID(z) computes the sigmoid of z.

% You need to return the following variables correctly 
g = zeros(size(z));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the sigmoid of each value of z (z can be a matrix,
%               vector or scalar).
%{
if size(z,1) == 1 && size(z,2) == 1
    g = 1 ./ (1+exp(-z));

elseif size(z,2) == 1
    for i = 1:length(z)
        g(i) = sigmoid(z(i));
    end
else
    for i = 1:size(z,2)
        g(:,i) = sigmoid(z(:,i));
    end 
end 
%}

g = 1 ./ (1+exp(-z)); 
% =============================================================
end
